from rest_framework import generics
from .serializers import RegisterSerializer
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class RegisterView(generics.CreateAPIView):
    User = get_user_model()

    serializer_class = RegisterSerializer
