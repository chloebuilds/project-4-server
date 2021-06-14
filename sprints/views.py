# from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Sprint
# , SprintGoal, Mood
from .serializers import SprintSerializer
# , SprintGoalSerializer, MoodSerializer

# Create your views here.
class SprintView(APIView):
    def get(self, _request):
        """Handle get requests on /sprints/ - index function"""
        # Get all sprints from the database
        sprints = Sprint.objects.all()
        print(sprints)
        # Serialize the data into JSON using the serializer.
        # Note the kwarg many=True which is necessary for sending back multiple objects.
        serialized_sprints = SprintSerializer(sprints, many=True)
        return Response(serialized_sprints.data, status=status.HTTP_200_OK)
  
    def post(self, request):
        new_sprint = SprintSerializer(data=request.data)
        if new_sprint.is_valid():
            new_sprint.save()
            return Response(new_sprint.errors, status=status.HTTP_201_CREATED)
        return Response(new_sprint.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# class SprintGoalView(APIView):
#     def post(self, request, sprint_pk):
#         request.data['sprint'] = sprint_pk
#         serialized_sprint_goal = SprintGoalSerializer(data=request.data)
#         if serialized_sprint_goal.is_valid():
#             serialized_sprint_goal.save()
#             return Response(serialized_sprint_goal.data, status=status.HTTP_201_CREATED)
#         return Response(serialized_sprint_goal.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


# class MoodView(APIView):
#     def post(self, request, sprint_pk):
#         request.data['sprint'] = sprint_pk
#         serialized_mood = MoodSerializer(data=request.data)
#         if serialized_mood.is_valid():
#             serialized_mood.save()
#             return Response(serialized_mood.data, status=status.HTTP_201_CREATED)
#         return Response(serialized_mood.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
