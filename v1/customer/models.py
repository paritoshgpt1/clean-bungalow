from django.db import models

# Create your models here.
class AbstractCustomer(models.Model):
	first_name = models.CharField(verbose_name='First Name', max_length=30, blank=True, null=True)
	last_name = models.CharField(verbose_name='Last Name', max_length=30, blank=True, null=True)
	username = models.CharField(verbose_name= 'Username', max_length= 50, blank = True, null = True)
	password = models.CharField(verbose_name= 'Password', max_length=50, blank = True, null=True)
	email = models.EmailField(verbose_name="Email", max_length=50, unique=True, null=True)

	class Meta:
		abstract = True
    

class Customer(AbstractCustomer):
	pass