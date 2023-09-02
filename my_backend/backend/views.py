from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from .models import WorkoutPlan
from .serializers import WorkoutPlanSerializer
from .models import NutritionPlan
from .serializers import NutritionPlanSerializer
# from rest_framework.generics import UpdateAPIView
# from .serializers import SelectWorkoutPlanSerializer

## for user
class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user_profile = UserProfile.objects.get(email=email, password=password)
        except UserProfile.DoesNotExist:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)

## for trainer

from .models import FitnessProfile
from .serializers import FitnessTrainerProfileSerializer

class FitnessTrainerProfileCreateView(generics.CreateAPIView):
    queryset = FitnessProfile.objects.all()
    serializer_class = FitnessTrainerProfileSerializer

class TrainerLoginView(generics.CreateAPIView):
    serializer_class = FitnessTrainerProfileSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user_profile = FitnessProfile.objects.get(email=email, password=password)
        except FitnessProfile.DoesNotExist:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)
    
##  workout plans
class WorkoutPlanCreateView(generics.CreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

class WorkoutPlanListView(generics.ListAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

class WorkoutPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

## Nutrition plans

class NutritionPlanCreateView(generics.CreateAPIView):
    queryset = NutritionPlan.objects.all()
    serializer_class = NutritionPlanSerializer

class NutritionPlanListView(generics.ListAPIView):
    queryset = NutritionPlan.objects.all()
    serializer_class = NutritionPlanSerializer

class NutritionPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NutritionPlan.objects.all()
    serializer_class = NutritionPlanSerializer




class SelectWorkoutPlanView(APIView):
    def patch(self, request, pk):
        try:
            # Get the user and workout plan instances based on their IDs
            user = UserProfile.objects.get(pk=pk)
            workout_plan_id = request.data.get('workout_plan_id')
            workout_plan = WorkoutPlan.objects.get(pk=workout_plan_id)

            # Assign the workout plan instance to the user's profile
            user.workout_plan_id = workout_plan
            user.save()

            return Response({'message': 'Workout plan updated successfully.'}, status=status.HTTP_200_OK)
        
        except UserProfile.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        except WorkoutPlan.DoesNotExist:
            return Response({'error': 'Workout plan not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# from .serializers import SelectNutritionPlanSerializer

class SelectNutritionPlanView(APIView):
    def patch(self, request, pk):
        try:
            # Get the user and nutrition plan instances based on their IDs
            user = UserProfile.objects.get(pk=pk)
            nutrition_plan_id = request.data.get('nutrition_plan_id')
            nutrition_plan = NutritionPlan.objects.get(pk=nutrition_plan_id)

            # Assign the nutrition plan instance to the user's profile
            user.nutrition_plan_id = nutrition_plan
            user.save()

            return Response({'message': 'Nutrition plan updated successfully.'}, status=status.HTTP_200_OK)
        
        except UserProfile.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        except NutritionPlan.DoesNotExist:
            return Response({'error': 'Nutrition plan not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

## get paln by id

class GetWorkoutPlanView(APIView):
    def get(self, request, workout_plan_id):
        try:
            # Retrieve the workout plan instance based on its ID
            workout_plan = WorkoutPlan.objects.get(pk=workout_plan_id)

            # Serialize the workout plan data using a serializer
            serializer = WorkoutPlanSerializer(workout_plan)

            # Return the serialized data as a JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)

        except WorkoutPlan.DoesNotExist:
            return Response({'error': 'Workout plan not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetNutritionPlanView(APIView):
    def get(self, request, nutrition_plan_id):
        try:
            # Retrieve the nutrition plan instance based on its ID
            nutrition_plan = NutritionPlan.objects.get(pk=nutrition_plan_id)

            # Serialize the nutrition plan data using a serializer
            serializer = NutritionPlanSerializer(nutrition_plan)

            # Return the serialized data as a JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)

        except NutritionPlan.DoesNotExist:
            return Response({'error': 'Nutrition plan not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
## get sigle user details

class GetUserByIdView(APIView):
    def get(self, request, user_id):
        try:
            # Retrieve the user instance based on their ID
            user = UserProfile.objects.get(pk=user_id)

            # Serialize the user data using a serializer
            serializer = UserProfileSerializer(user)

            # Return the serialized data as a JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)

        except UserProfile.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)