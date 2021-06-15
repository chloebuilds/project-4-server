from rest_framework import serializers
from .models import Sprint, Mood, SprintGoal, Energy

class EnergySerializer(serializers.ModelSerializer):

    class Meta:
        model = Energy
        fields = '__all__'

class MoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mood
        fields = '__all__'

class SprintGoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = SprintGoal
        fields = '__all__'

class SprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprint
        fields = '__all__'

class PopulatedSprintSerializer(SprintSerializer):

    SprintGoal = SprintGoalSerializer(many=True)
    Mood = MoodSerializer(many=True)
    Energy = EnergySerializer(many=True)
