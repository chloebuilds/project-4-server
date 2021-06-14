from rest_framework import serializers
from .models import Sprint
# Mood, SprintGoal, 

# class MoodSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Mood
#         fields = '__all__'

# class SprintGoalSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = SprintGoal
#         fields = '__all__'

class SprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprint
        fields = '__all__'

# class PopulatedSprintSerializer(SprintSerializer):

#     SprintGoal = SprintSerializer(many=True)
#     Mood = SprintSerializer(many=True)
