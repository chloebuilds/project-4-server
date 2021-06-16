from datetime import date, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Sprint, SprintGoal, SprintHabit, DailyToDo,  DailyMood, DailyEnergy, DailyGratitude, WeeklyIntention
from .serializers import SprintHabitSerializer, SprintGoalSerializer 
from .serializers import SprintSerializer, PopulatedSprintSerializer
from .serializers import DailyToDoSerializer, DailyMoodSerializer,  DailyEnergySerializer, DailyGratitudeSerializer 
from .serializers import WeeklyIntentionSerializer



#! SPRINT LIST VIEW // CHANGE THIS //

class SprintListView(APIView):
    permission_classes = (IsAuthenticated, )
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

#! SPRINT VIEW 

class SprintDetailView(APIView):
    permission_classes = (IsAuthenticated, )
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
 

#! DAILY VIEWS

#* Daily To-Do 
class DailyToDoListView(APIView):  
    #GET ALL TO-DOs
    def get(self, _request):
        all_to_dos = DailyToDo.objects.all()
        serialized_all_to_dos = DailyToDoSerializer(all_to_dos, many=True)
        return Response(serialized_all_to_dos.data, status=status.HTTP_200_OK)
    #POST A TO-DO 
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data["end_date"] = date.today() + timedelta(days=0)
        serialized_to_do = DailyToDoSerializer(data = request.data)
        if serialized_to_do.is_valid():
            serialized_to_do.save()
            return Response(serialized_to_do.data, status=status.HTTP_201_CREATED)
        return Response(serialized_to_do.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class DailyToDoDetailView(APIView):     
    #DELETE A TO-DO
    def delete(self, _request, _sprint_pk, to_do_pk):
        # try:
        to_do_to_delete = DailyToDo.objects.get(pk=to_do_pk)
        to_do_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #UPDATE A TO-DO
    def put(self, request, to_do_pk):
        to_do_to_update = DailyToDo.objects.get(pk=to_do_pk)
        updated_to_do = DailyToDoSerializer(to_do_to_update, data=request.data)
        if updated_to_do.is_valid():
            updated_to_do.save()
            return Response(updated_to_do.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_to_do.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#* Daily Mood
class DailyMoodListView(APIView):
    #GET ALL MOODS
    def get(self, _request):
        all_moods = DailyMood.objects.all()
        serialized_moods = DailyMoodSerializer(all_moods, many=True)
        return Response(serialized_moods.data, status=status.HTTP_200_OK)
    #POST A MOOD
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data["end_date"] = date.today() + timedelta(days=0)
        serialized_mood = DailyMoodSerializer(data=request.data)
        if serialized_mood.is_valid():
            serialized_mood.save()
            return Response(serialized_mood.data, status=status.HTTP_201_CREATED)
        return Response(serialized_mood.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class DailyMoodDetailView(APIView): 
    #DELETE A MOOD
    def delete(self, _request, _sprint_pk, mood_pk):
        mood_to_delete = DailyMood.objects.get(pk=mood_pk)
        mood_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#* Daily Energy Level
class DailyEnergyListView(APIView):
    #GET ALL ENERGY LEVELS
    def get(self, _request):
        all_energy_levels = DailyEnergy.objects.all()
        serialized_energy_levels = DailyEnergySerializer(all_energy_levels, many=True)
        return Response(serialized_energy_levels.data, status=status.HTTP_200_OK)
    #POST AN ENERGY LEVEL
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data["end_date"] = date.today() + timedelta(days=0)
        serialized_energy = DailyEnergySerializer(data=request.data)
        if serialized_energy.is_valid():
            serialized_energy.save()
            return Response(serialized_energy.data, status=status.HTTP_201_CREATED)
        return Response(serialized_energy.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class DailyEnergyDetailView(APIView):
    #DELETE ENERGY LEVEL
    def delete(self, _request, _sprint_pk, energy_level_pk):
        energy_level_to_delete = DailyEnergy.objects.get(pk=energy_level_pk)
        energy_level_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #UPDATE ENERGY LEVEL
    def put(self, request, energy_level_pk):
        energy_level_to_update = DailyEnergy.objects.get(pk=energy_level_pk)
        updated_energy_level = DailyEnergySerializer(energy_level_to_update, data=request.data)
        if updated_energy_level.is_valid():
            updated_energy_level.save()
            return Response(updated_energy_level.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_energy_level.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#* Daily Gratitude
class DailyGratitudeListView(APIView):
    #GET ALL GRATITUDES
    def get(self, _request):
        all_gratitudes = DailyGratitude.objects.all()
        serialized_gratitudes = DailyGratitudeSerializer (all_gratitudes, many=True)
        return Response(serialized_gratitudes.data, status=status.HTTP_200_OK)
    #POST GRATITUDE 
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data["end_date"] = date.today() + timedelta(days=0)
        serialized_gratitude = DailyGratitudeSerializer(data=request.data)
        if serialized_gratitude.is_valid():
            serialized_gratitude.save()
            return Response(serialized_gratitude.data, status=status.HTTP_201_CREATED)
        return Response(serialized_gratitude.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class DailyGratitudeDetailView(APIView):
    #DELETE GRATITUDE 
    def delete(self, _request, _sprint_pk, gratitude_pk):
        gratitude_to_delete = DailyGratitude.objects.get(pk=gratitude_pk)
        gratitude_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #UPDATE GRATITUDE 
    def put(self, request, gratitude_pk):
        gratitude_to_update = DailyGratitude.objects.get(pk=gratitude_pk)
        updated_gratitude = DailyGratitudeSerializer(gratitude_to_update, data=request.data)
        if updated_gratitude.is_valid():
            updated_gratitude.save()
            return Response(updated_gratitude.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_gratitude.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#! WEEKLY VIEWS

#* Weekly Intentions
class WeeklyIntentionListView(APIView):
    #GET ALL INTENTIONS
    def get(self, _request):
        all_intentions = WeeklyIntention.objects.all()
        serialized_intentions = WeeklyIntentionSerializer (all_intentions, many=True)
        return Response(serialized_intentions.data, status=status.HTTP_200_OK)
    #POST AN INTENTION
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data["end_date"] = date.today() + timedelta(days=6)
        serialized_intention = WeeklyIntentionSerializer(data=request.data)
        if serialized_intention.is_valid():
            serialized_intention.save()
            return Response(serialized_intention.data, status=status.HTTP_201_CREATED)
        return Response(serialized_intention.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class WeeklyIntentionDetailView(APIView):   
    #DELETE  AN INTENTION
    def delete(self, _request, _sprint_pk, intention_pk):
        intention_to_delete = WeeklyIntention.objects.get(pk=intention_pk)
        intention_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #UPDATE AN INTENTION
    def put(self, request, intention_pk):
        intention_to_update = WeeklyIntention.objects.get(pk=intention_pk)
        updated_intention = WeeklyIntentionSerializer(intention_to_update, data=request.data)
        if updated_intention.is_valid():
            updated_intention.save()
            return Response(updated_intention.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_intention.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#! SPRINT-LENGTH VIEWS

#* Sprint Habits
class SprintHabitListView(APIView):
    #GET ALL HABITS
    def get(self, _request):
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
    def delete(self, _request, _sprint_pk, sprint_habit_pk):
        sprint_habit_to_delete = SprintHabit.objects.get(pk=sprint_habit_pk)
        sprint_habit_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #UPDATE A HABIT
    def put(self, request, sprint_habit_pk):
        sprint_habit_to_update = SprintHabit.objects.get(pk=sprint_habit_pk)
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
    def delete(self, _request, _sprint_pk, sprint_goal_pk):
        sprint_goal_to_delete = SprintGoal.objects.get(pk=sprint_goal_pk)
        sprint_goal_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #UPDATE A GOAL
    def put(self, request, sprint_goal_pk):
        sprint_goal_to_update = SprintGoal.objects.get(pk=sprint_goal_pk)
        updated_sprint_goal = SprintGoalSerializer(sprint_goal_to_update, data=request.data)
        if updated_sprint_goal.is_valid():
            updated_sprint_goal.save()
            return Response(updated_sprint_goal.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_sprint_goal.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

