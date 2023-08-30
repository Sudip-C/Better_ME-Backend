from rest_framework import serializers
from .models import UserProfile
from .models import FitnessProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class FitnessTrainerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessProfile
        fields = '__all__'