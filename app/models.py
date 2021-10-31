from django.db import models
from django.contrib.auth.models import User
from tinymyce

# Create your models here.
Priority=(
    ('Low Priority','Low Priority'),
    ('High Priority','High Priority'),
)

class neighborhood(models.Model):
	neighborhood= models.CharField(max_length=100)

	def __str__(self):
		return self.neighborhood

	def create_neighborhood(self):
		self.save()

	@classmethod
	def delete_neighborhood(cls,neighborhood):
		cls.objects.filter(neighborhood = neighborhood).delete()

class Profile(models.Model):
	profpic = CloudinaryField('image')
	description = HTMLField()
	neighborhood = models.ForeignKey(neighborhood,on_delete=models.CASCADE)
	username = models.ForeignKey(User,on_delete=models.CASCADE)
	name =models.CharField(max_length=100)
	email = models.EmailField()

	def __str__(self):
		return self.name