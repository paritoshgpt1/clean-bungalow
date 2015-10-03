from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(verbose_name='First Name', max_length=30, blank=True, null=True)
	last_name = models.CharField(verbose_name='Last Name', max_length=30, blank=True, null=True)
	