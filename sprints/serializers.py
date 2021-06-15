from rest_framework import serializers
from .models import SprintGoal, SprintHabit, Sprint
from .models import WeeklyIntention
from .models import Energy, DailyToDo, Mood, DailyGratitude


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
    SprintGoal = SprintGoalSerializer(many=True)
    Mood = MoodSerializer(many=True)
    Energy = EnergySerializer(many=True)
