from rest_framework import serializers
from .models import SprintGoal, SprintHabit, DailyToDo, Sprint, Mood


#! DAILY SERIALIZERS

class DailyToDoSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = DailyToDo
        fields = '__all__'

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'

#! WEEKLY SERIALIZERS

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
    SprintGoal = SprintSerializer(many=True)
    Mood = SprintSerializer(many=True)