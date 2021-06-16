from rest_framework import serializers
from django.contrib.auth import get_user_model


from .models import SprintGoal, SprintHabit, Sprint
from .models import WeeklyIntention
from .models import Energy, DailyToDo, Mood, DailyGratitude

User = get_user_model()

#! USER SERIALIZERS
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'avatar')

#! DAILY SERIALIZERS
class DailyToDoSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = DailyToDo
        fields = '__all__'


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'

class GratitudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGratitude
        fields = '__all__'

class EnergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Energy
        fields = '__all__'

#! WEEKLY SERIALIZERS
class IntentionSerializer(serializers.ModelSerializer):
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
    moods = MoodSerializer(many=True)
    energy_levels = EnergySerializer(many=True)
    daily_to_do = DailyToDoSerializer(many=True)
    daily_gratitudes = GratitudeSerializer(many=True)
    weekly_intentions = IntentionSerializer(many=True)
    sprint_habits = SprintHabitSerializer(many=True)

