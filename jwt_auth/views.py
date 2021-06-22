from datetime import datetime, timedelta
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from datetime import datetime, date, timedelta
from django.contrib.auth import get_user_model
from django.conf import settings

import jwt

from .serializers import UserSerializer
from .populated import PopulatedUserSerializer
from sprints.serializers import SprintSerializer

User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        # Run the body of the request through the serializer for serialization and validation
        user_to_create = UserSerializer(data=request.data)

        # Proceed if valid
        if user_to_create.is_valid():
            user_to_create.save()
            return Response({"message": "Registration Successful"}, status=status.HTTP_201_CREATED)

        # Send back 422 if not valid
        return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(APIView):
    def post(self, request):
        # Get the email and password from the body of the request
        email = request.data.get("email")
        password = request.data.get("password")

        # Use the email to try and find the User in the database
        try:
            user_to_login = User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied()
        # Now we have the user, we can check their password
        # The `check_password` method comes from AbstractUser
        if not user_to_login.check_password(password):
            raise PermissionDenied()

        # Calculate the expiry time by taking the current time and adding 7 days to it
        expiry_time = datetime.now() + timedelta(days=7)

        # Create the token to send back using jwt
        token = jwt.encode(
            {
                # This will be the "subject" of the token
                # i.e. the user in the form of their primary_key/id
                "sub": user_to_login.id,
                # This converts the expiry time to a UNIX timestamp
                "exp": int(expiry_time.strftime("%s")),
            },
            settings.SECRET_KEY,
            algorithm="HS256",
        )

        # Send back a positive response if login is OK
        return Response({"token": token, "message": f"Welcome back, {user_to_login.username}"})

# We will use this to get a user's profile for the dashboard
class ProfileView(APIView):
    def get(self, _request, pk):
        try:
            # Find the user
            user_to_show = User.objects.get(pk=pk)
            # Serialize the user using the dedicated PopulatedUserSerializer
            serialized_user = PopulatedUserSerializer(user_to_show)
            # Return a 200 with the use
            return Response(serialized_user.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            raise NotFound()

class ResetView(APIView):
    def put(self, _request, pk):
        user = User.objects.get(pk=pk)
        sprints = list(user.created_sprints.all())

        current_sprint = None
        todays_date = date.today()

        # Establish which is the current sprint
        for sprint in sprints:
            if sprint.end_date > todays_date:
                current_sprint = sprint

        # If no current sprint, there user will have to create a new sprint anyway
        # So nothing to unlink
        if not current_sprint:
            serialized_user = PopulatedUserSerializer(user)
            return Response(serialized_user.data, status=status.HTTP_202_ACCEPTED)

        moods = list(current_sprint.moods.all())
        energy_levels = list(current_sprint.energy_levels.all())
        to_dos = list(current_sprint.to_dos.all())
        daily_gratitudes = list(current_sprint.daily_gratitudes.all())
        weekly_intentions = list(current_sprint.weekly_intentions.all())

        # Iterate through the goalsets and remove the reference to the current sprint 
        # if the goal end_date is in the past
        for goalset in [moods, energy_levels, to_dos, daily_gratitudes, weekly_intentions]:
            if goalset:
                for goal in goalset:
                    if goal.end_date < todays_date:
                        goal.sprint = None
                        goal.save()
        
        serialized_updated_user = PopulatedUserSerializer(user)
        return Response(serialized_updated_user.data, status=status.HTTP_200_OK)