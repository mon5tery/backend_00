from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=400)

	def __str__(self):
		return '%s %s' % (self.id, self.user)

# For saving Profile

@receiver(post_save, sender=User)
def profile_creation(instance, created, *args, **kwargs):
	if created:
		Profile.objects.create(user=instance)