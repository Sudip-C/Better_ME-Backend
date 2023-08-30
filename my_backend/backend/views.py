from rest_framework import generics,status
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer

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