# We'll use a different serializer and keep our main UserSerializer
# purely for the purposes of sending back populated users for profiles, etc.
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from sprints.serializers import PopulatedSprintSerializer


User = get_user_model()

class PopulatedUserSerializer(ModelSerializer):
    created_sprints = PopulatedSprintSerializer(many=True)
    class Meta:
        model = User
        fields = ("id", "username", "name", "avatar", "dark_mode", "created_sprints")