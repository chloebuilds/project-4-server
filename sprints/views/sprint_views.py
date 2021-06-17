from datetime import date, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
#? from rest_framework.permissions import IsAuthenticated
#? from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from ..models import Sprint
from ..serializers import SprintSerializer, PopulatedSprintSerializer


#! SPRINT LIST VIEW

class SprintListView(APIView):
    #? permission_classes = (IsAuthenticated, )
    #GET ALL SPRINTS
    def get(self, _request):
        # Get all sprints from the database
        sprints = Sprint.objects.all()
        serialized_sprints = PopulatedSprintSerializer(sprints, many=True)
        return Response(serialized_sprints.data, status=status.HTTP_200_OK)
        
    #POST A SPRINT
    def post(self, request):
        request.data["end_date"] = date.today() + timedelta(days=27)
        request.data['owner'] = request.user.id
        new_sprint = SprintSerializer(data=request.data)
        if new_sprint.is_valid():
            new_sprint.save()
            return Response(new_sprint.data, status=status.HTTP_201_CREATED)
        return Response(new_sprint.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#! SPRINT DETAIL VIEW 

class SprintDetailView(APIView):

    #? permission_classes = (IsAuthenticated, )

    #GET A SINGLE SPRINT
    def get_sprint(self, pk):
        try:
            return Sprint.objects.get(pk=pk)
        except Sprint.DoesNotExist:
            raise NotFound()
    def get(self, _request, pk):
        sprint = self.get_sprint(pk=pk)
        serialized_sprint = PopulatedSprintSerializer(sprint)
        return Response(serialized_sprint.data, status=status.HTTP_200_OK)
    #UPDATE A SPRINT
    def put(self, request, pk):
        sprint_to_update = self.get_sprint(pk=pk)
        request.data['owner'] = request.user.id
        request.data['end_date'] = Sprint.objects.get(pk=pk).end_date
        updated_sprint = SprintSerializer(sprint_to_update, data=request.data)
        if updated_sprint.is_valid():
            updated_sprint.save()
            return Response(updated_sprint.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_sprint.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    #DELETE A SPRINT   
    def delete(self, _request, pk):
        sprint_to_delete = self.get_sprint(pk=pk)
        sprint_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


