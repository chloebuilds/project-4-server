from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import SprintGoal, SprintHabit, DailyToDo, Sprint, Mood
from .serializers import DailyToDoSerializer, MoodSerializer, SprintHabitSerializer, SprintGoalSerializer, SprintSerializer, PopulatedSprintSerializer

#! SPRINT VIEW

#! DAILY VIEWS
#* Daily To-Do 
class DailyToDoListView(APIView):   
    #POST A TO-DO 
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data["end_date"] = datetime.date.today() + timedelta(days=0)
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
#POST ENERGY LEVEL
#DELETE ENERGY LEVEL
#* Daily Gratitude
#POST GRATITUDE 
#DELETE GRATITUDE 

#! WEEKLY VIEWS
#* Weekly Intentions
#POST AN INTENTION
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
        serialized_sprint_goal = SprintGoalSerializer(data=request.data)
        if serialized_sprint_goal.is_valid():
            serialized_sprint_goal.save()
            return Response(serialized_sprint_goal.data, status=status.HTTP_201_CREATED)
        return Response(serialized_sprint_goal.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    #DELETE A GOAL
