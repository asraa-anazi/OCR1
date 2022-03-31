from django.db import models

# Create your models here.

class filename1(models.Model):
	FBS = models.CharField(max_length=100, blank=True)
	doument = models.FileField(upload_to='media/')
	uploaded_at = models.DateTimeField(auto_now_add=True)	


	def __str__(self):
		return self.FBS