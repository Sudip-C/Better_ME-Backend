from rest_framework import serializers
from .models import UserProfile
from .models import FitnessProfile
from .models import WorkoutPlan
from .models import NutritionPlan

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class FitnessTrainerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessProfile
        fields = '__all__'

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'

class NutritionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionPlan
        fields = '__all__'

class SelectWorkoutPlanSerializer(serializers.Serializer):
    workout_plan_id = serializers.IntegerField(required=True)

class SelectNutritionPlanSerializer(serializers.Serializer):
    nutrition_plan_id = serializers.IntegerField(required=True)