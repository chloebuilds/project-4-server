from datetime import date, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
#? from rest_framework.permissions import IsAuthenticated
#? from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from ..models import SprintGoal, SprintHabit
from ..serializers import SprintHabitSerializer, SprintGoalSerializer 

#! SPRINT-LENGTH VIEWS

#* Sprint Habits
class SprintHabitListView(APIView):
    #GET ALL HABITS
    def get(self, _request, sprint_pk):
        all_sprint_habits = SprintHabit.objects.all()
        serialized_sprint_habits = SprintHabitSerializer (all_sprint_habits, many=True)
        return Response(serialized_sprint_habits.data, status=status.HTTP_200_OK)
    #POST A HABIT
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data["end_date"] = date.today() + timedelta(days=27)
        serialized_sprint_habit = SprintHabitSerializer(data=request.data)
        if serialized_sprint_habit.is_valid():
            serialized_sprint_habit.save()
            return Response(serialized_sprint_habit.data, status=status.HTTP_201_CREATED)
        return Response(serialized_sprint_habit.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class SprintHabitDetailView(APIView):
    #GET A SINGLE HABIT
    def get_goal(self, pk):
        try:
            return SprintHabit.objects.get(pk=pk)
        except SprintHabit.DoesNotExist:
            raise NotFound()

    def get(self, _request, sprint_pk, sprint_habit_pk):
        sprint_habit = self.get_goal(pk=sprint_habit_pk)
        serialized_sprint_habit = SprintHabitSerializer(sprint_habit)
        return Response(serialized_sprint_habit.data, status=status.HTTP_200_OK)
    #DELETE A HABIT
    def delete(self, _request, sprint_pk, sprint_habit_pk):
        sprint_habit_to_delete = SprintHabit.objects.get(pk=sprint_habit_pk)
        sprint_habit_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #UPDATE A HABIT
    def put(self, request, sprint_pk, sprint_habit_pk):
        sprint_habit_to_update = SprintHabit.objects.get(pk=sprint_habit_pk)
        request.data['sprint'] = sprint_pk
        request.data['owner'] = request.user.id
        request.data['end_date'] = SprintHabit.objects.get(pk=sprint_habit_pk).end_date
        updated_sprint_habit = SprintHabitSerializer(sprint_habit_to_update, data=request.data)
        if updated_sprint_habit.is_valid():
            updated_sprint_habit.save()
            return Response(updated_sprint_habit.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_sprint_habit.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#* Sprint Goals
class SprintGoalListView(APIView):
    #GET ALL GOALS
    def get(self, _request, sprint_pk):
        all_sprint_goals = SprintGoal.objects.all()
        serialized_sprint_goals = SprintGoalSerializer (all_sprint_goals, many=True)
        return Response(serialized_sprint_goals.data, status=status.HTTP_200_OK)
    #POST A GOAL
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data["end_date"] = date.today() + timedelta(days=27)
        serialized_sprint_goal = SprintGoalSerializer(data=request.data)
        if serialized_sprint_goal.is_valid():
            serialized_sprint_goal.save()
            return Response(serialized_sprint_goal.data, status=status.HTTP_201_CREATED)
        return Response(serialized_sprint_goal.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class SprintGoalDetailView(APIView):
    #GET A SINGLE GOAL
    def get_goal(self, pk):
        try:
            return SprintGoal.objects.get(pk=pk)
        except SprintGoal.DoesNotExist:
            raise NotFound()

    def get(self, _request, sprint_pk, sprint_goal_pk):
        sprint_goal = self.get_goal(pk=sprint_goal_pk)
        serialized_sprint_goal = SprintGoalSerializer(sprint_goal)
        return Response(serialized_sprint_goal.data, status=status.HTTP_200_OK)
    #DELETE A GOAL
    def delete(self, _request, sprint_pk, sprint_goal_pk):
        sprint_goal_to_delete = SprintGoal.objects.get(pk=sprint_goal_pk)
        sprint_goal_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #UPDATE A GOAL
    def put(self, request, sprint_pk, sprint_goal_pk):
        sprint_goal_to_update = SprintGoal.objects.get(pk=sprint_goal_pk)
        request.data['sprint'] = sprint_pk
        request.data['owner'] = request.user.id
        request.data['end_date'] = SprintGoal.objects.get(pk=sprint_goal_pk).end_date
        updated_sprint_goal = SprintGoalSerializer(sprint_goal_to_update, data=request.data)
        if updated_sprint_goal.is_valid():
            updated_sprint_goal.save()
            return Response(updated_sprint_goal.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_sprint_goal.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
