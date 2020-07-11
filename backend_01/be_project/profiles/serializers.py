from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class UserCreateSerializer(serializers.ModelSerializer):
	password =serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'last_name', 'email', ]

		def create(self, validated_data):
			username = validated_data['username']
			password = validated_data['password']
			first_name = validated_data['first_name']
			last_name = validated_data['last_name']
			email = validated_data['email']
			new_user = User(username=username, first_name=first_name, last_name=last_name, email=email, bio=bio)
			new_user.set_password(password)
			new_user.save()

			return validated_data

		def validate_email(self, email):
			user = User.objects.filters(email=email)
			if user:
				raise serializers.ValidationError('Email Exits.')
			return email

# Checking email ?

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', ]

class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	
	class Meta:
		model = Profile
		fields = ['user', 'pic' ]

	def get_username(self, obj):
		return '%s' % (obj.user.username)
