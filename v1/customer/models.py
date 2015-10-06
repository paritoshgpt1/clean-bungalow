from django.db import models

# Create your models here.
class AbstractCustomer(models.Model):
	first_name = models.CharField(verbose_name='First Name', max_length=30, blank=True, null=True)
	last_name = models.CharField(verbose_name='Last Name', max_length=30, blank=True, null=True)
	username = models.CharField(verbose_name= 'Username', max_length= 50, blank = True, null = True)
	password = models.CharField(verbose_name= 'Password', max_length=50, blank = True, null=True)
	email = models.EmailField(verbose_name="Email", max_length=50, unique=True, null=True)
	mob_no = models.CharField(verbose_name= 'Mobile No', max_length=50, blank = True, null=True)
	shipping_address = models.CharField(verbose_name= 'Shipping Address', max_length=50, blank = True, null=True)
	billing_address = models.CharField(verbose_name= 'Billing Address', max_length=50, blank = True, null=True)

class AbstractAddress(models.Model):
	line_one = models.CharField(verbose_name='Address Line 1', max_length=30, blank=True, null=True)
	line_two = models.CharField(verbose_name='Address Line 2', max_length=30, blank=True, null=True)
	city = models.CharField(verbose_name='City', max_length=30, blank=True, null=True)
	State = models.CharField(verbose_name='First Name', max_length=30, blank=True, null=True)
	landmark = models.CharField(verbose_name='First Name', max_length=30, blank=True, null=True)
	locality = models.CharField(verbose_name='First Name', max_length=30, blank=True, null=True)
	pincode = models.IntegerField(verbose_name='First Name', max_length=30, blank=True, null=True)


	class Meta:
		abstract = True
    

class Customer(AbstractCustomer):
	pass

class Address(AbstractAddress):
	pass

class OrderCustomer(AbstractCustomer):
	pass
		
class OrderAddress(AbstractAddress):
	pass


	
	