from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import ProfileCreateSerializer, ProfileSerializer
from .models import Profile

# Create your views here.

class ProfileCreateView(CreateAPIView):
	serializer_class = ProfileCreateSerializer

class ProfileView(RetrieveAPIView):
	serializer_class = ProfileSerializer

	def get_object(self):
		return self.request.user.Profile

