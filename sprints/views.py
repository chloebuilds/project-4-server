from datetime import date, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import SprintGoal, SprintHabit, DailyToDo, Sprint, Mood
from .serializers import DailyToDoSerializer, MoodSerializer,  EnergySerializer, GratitudeSerializer 
from .serializers import IntentionSerializer
from .serializers import SprintHabitSerializer, SprintGoalSerializer, SprintSerializer, PopulatedSprintSerializer

#! SPRINT VIEW
class SprintView(APIView):
    # GET ALL SPRINT
    def get(self, _request):
        sprints = Sprint.objects.all()
        print(sprints)
        serialized_sprints = SprintSerializer(sprints, many=True)
        return Response(serialized_sprints.data, status=status.HTTP_200_OK)
    
    #POST A SPRINT
    def post(self, request):
        request.data["end_date"] = date.today() + timedelta(days=27)
        new_sprint = SprintSerializer(data=request.data)
        if new_sprint.is_valid():
            new_sprint.save()
            return Response(new_sprint.errors, status=status.HTTP_201_CREATED)
        return Response(new_sprint.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SprintDetailView(APIView):

    def get_sprint(self, pk):
        try:
            return Sprint.objects.get(pk=pk)
        except Sprint.DoesNotExist:
            raise NotFound()

    def get(self, _request, pk):
        sprint = self.get_sprint(pk=pk)
        serialized_sprint = SprintSerializer(sprint)
        return Response(serialized_sprint.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        sprint_to_update = self.get_sprint(pk=pk)
        updated_sprint = SprintSerializer(sprint_to_update, data=request.data)
        if updated_sprint.is_valid():
            updated_sprint.save()
            return Response(updated_sprint.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_sprint.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    def delete(self, _request, pk):
        sprint_to_delete = self.get_sprint(pk=pk)
        sprint_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
  
#! DAILY VIEWS
#* Daily To-Do 
class DailyToDoListView(APIView):   
    #POST A TO-DO 
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data["end_date"] = date.today() + timedelta(days=0)
        serialized_to_do = DailyToDoSerializer(data = request.data)
        if serialized_to_do.is_valid():
            serialized_to_do.save()
            return Response(serialized_to_do.data, status=status.HTTP_201_CREATED)
        return Response(serialized_to_do.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    #DELETE A TO-DO
    def delete(self, _request, _sprint_pk, to_do_pk):
        # try:
        to_do_to_delete = DailyToDo.objects.get(pk=to_do_pk)
        to_do_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        #TODO except DailyToDo.DoesNotExist:
        #TODO     raise NotFound()
    #UPDATE A TO-DO
    def put(self, request, to_do_pk):
        to_do_to_update = DailyToDo.objects.get(pk=to_do_pk)
        updated_to_do = DailyToDoSerializer(to_do_to_update, data=request.data)
        if updated_to_do.is_valid():
            updated_to_do.save()
            return Response(updated_to_do.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_to_do.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#* Daily Mood
class MoodView(APIView):
    #POST A MOOD
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        serialized_mood = MoodSerializer(data=request.data)
        if serialized_mood.is_valid():
            serialized_mood.save()
            return Response(serialized_mood.data, status=status.HTTP_201_CREATED)
        return Response(serialized_mood.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    #DELETE A MOOD

#* Daily Energy Level
class EnergyView(APIView):
    #POST ENERGY LEVEL
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        serialized_energy = EnergySerializer(data=request.data)
        if serialized_energy.is_valid():
            serialized_energy.save()
            return Response(serialized_energy.data, status=status.HTTP_201_CREATED)
        return Response(serialized_energy.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
#DELETE ENERGY LEVEL

#* Daily Gratitude
class GratitudeView(APIView):
    #POST GRATITUDE 
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        serialized_gratitude = GratitudeSerializer(data=request.data)
        if serialized_gratitude.is_valid():
            serialized_gratitude.save()
            return Response(serialized_gratitude.data, status=status.HTTP_201_CREATED)
        return Response(serialized_gratitude.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
#DELETE GRATITUDE 

#! WEEKLY VIEWS
#* Weekly Intentions
class IntentionView(APIView):
    #POST AN INTENTION
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        serialized_intention = IntentionSerializer(data=request.data)
        if serialized_intention.is_valid():
            serialized_intention.save()
            return Response(serialized_intention.data, status=status.HTTP_201_CREATED)
        return Response(serialized_intention.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    #TODO def put(self, request, sprint_pk)
    #TODO intention_to_update = self.intention
    #UPDATE AN INTENTION
    #DELETE AN INTENTION

#! SPRINT-LENGTH VIEWS
#* Sprint Habits
#POST A HABIT
#DELETE A HABIT
#* Sprint Goals
class SprintGoalView(APIView):
    #POST A GOAL
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data["end_date"] = date.today() + timedelta(days=27)
        serialized_sprint_goal = SprintGoalSerializer(data=request.data)
        if serialized_sprint_goal.is_valid():
            serialized_sprint_goal.save()
            return Response(serialized_sprint_goal.data, status=status.HTTP_201_CREATED)
        return Response(serialized_sprint_goal.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    #DELETE A GOAL
