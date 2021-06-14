from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Sprint
from .serializers import SprintSerializer

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