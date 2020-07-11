from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import UserCreateSerializer, ProfileSerializer
from .models import Profile

# Create your views here.

class UserCreateView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ProfileView(RetrieveAPIView):
	serializer_class = ProfileSerializer

	def get_object(self):
		return self.request.user.profile

