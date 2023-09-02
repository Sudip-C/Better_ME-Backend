from django.urls import path
from .views import GetUserByIdView,UserProfileCreateView,UserLoginView,FitnessTrainerProfileCreateView,TrainerLoginView,WorkoutPlanCreateView, WorkoutPlanListView, WorkoutPlanDetailView,NutritionPlanCreateView, NutritionPlanListView, NutritionPlanDetailView,SelectWorkoutPlanView, SelectNutritionPlanView,GetWorkoutPlanView


urlpatterns = [
    path('user-signup/', UserProfileCreateView.as_view(), name='user-signup'),
    path('user-login/', UserLoginView.as_view(), name='user-login'),
    path('trainer-signup/', FitnessTrainerProfileCreateView.as_view(), name='trainer-signup'),
    path('trainer-login/', TrainerLoginView.as_view(), name='trainer-login'),
    path('workout-plans/', WorkoutPlanListView.as_view(), name='workoutplan-list'),
    path('workout-plans/<int:pk>/', WorkoutPlanDetailView.as_view(), name='workoutplan-detail'),
    path('workout-plans/create/', WorkoutPlanCreateView.as_view(), name='workoutplan-create'),
    path('nutrition-plans/', NutritionPlanListView.as_view(), name='nutritionplan-list'),
    path('nutrition-plans/<int:pk>/', NutritionPlanDetailView.as_view(), name='nutritionplan-detail'),
    path('nutrition-plans/create/', NutritionPlanCreateView.as_view(), name='nutritionplan-create'),
    path('users/<int:pk>/select-workout-plan/', SelectWorkoutPlanView.as_view(), name='select-workout-plan'),
    path('users/<int:pk>/select-nutrition-plan/', SelectNutritionPlanView.as_view(), name='select-nutrition-plan'),
    path('workout-plans/<int:workout_plan_id>/', GetWorkoutPlanView.as_view(), name='get-workout-plan'),
    path('nutrition-plans/<int:nutrition_plan_id>/', GetWorkoutPlanView.as_view(), name='get-workout-plan'),
    path('users/<int:user_id>/', GetUserByIdView.as_view(), name='get-user-by-id'),
]
