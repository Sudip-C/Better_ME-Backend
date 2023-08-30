from django.urls import path
from .views import UserProfileCreateView,UserLoginView,FitnessTrainerProfileCreateView,TrainerLoginView

urlpatterns = [
    path('user-signup/', UserProfileCreateView.as_view(), name='user-signup'),
    path('user-login/', UserLoginView.as_view(), name='user-login'),
    path('trainer-signup/', FitnessTrainerProfileCreateView.as_view(), name='trainer-signup'),
    path('trainer-login/', TrainerLoginView.as_view(), name='trainer-login'),
]
