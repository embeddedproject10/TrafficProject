from django.db import models

# Create your models here.
class Places(models.Model):
	place_name = models.CharField(max_length=50)
	crowded = models.CharField(max_length=5,default="yes")

	def __str__(self):
		return self.crowded
	def __str__(self):
		return self.place_name





