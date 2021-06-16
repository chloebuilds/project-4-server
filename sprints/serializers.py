from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Sprint, SprintGoal, SprintHabit
from .models import WeeklyIntention
from .models import DailyEnergy,  DailyMood, DailyGratitude, DailyToDo


#! USER SERIALIZERS
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'avatar')

#! DAILY SERIALIZERS
class DailyToDoSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = DailyToDo
        fields = '__all__'


class DailyMoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMood
        fields = '__all__'

class DailyGratitudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGratitude
        fields = '__all__'

class DailyEnergySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyEnergy
        fields = '__all__'

#! WEEKLY SERIALIZERS
class WeeklyIntentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyIntention
        fields = '__all__'
        
#! SPRINT-LENGTH SERIALIZERS
class SprintHabitSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = SprintHabit
        fields = '__all__'

class SprintGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprintGoal
        fields = '__all__'

#! SPRINT SERIALIZERS
class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'
        
class PopulatedSprintSerializer(SprintSerializer):
    owner = UserSerializer()
    sprint_goals = SprintGoalSerializer(many=True)
    moods = DailyMoodSerializer(many=True)
    energy_levels = DailyEnergySerializer(many=True)
    to_dos = DailyToDoSerializer(many=True)
    daily_gratitudes = DailyGratitudeSerializer(many=True)
    weekly_intentions = WeeklyIntentionSerializer(many=True)
    sprint_habits = SprintHabitSerializer(many=True)
