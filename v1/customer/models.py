from django.db import models



class AbstractCustomer(models.Model):
	first_name = models.CharField(verbose_name='First Name', max_length=30, blank=True, null=True)
	last_name = models.CharField(verbose_name='Last Name', max_length=30, blank=True, null=True)
	username = models.CharField(verbose_name='Username', max_length=50, blank=True, null=True)
	password = models.CharField(verbose_name='Password', max_length=50, blank=True, null=True)
	email = models.EmailField(verbose_name="Email", max_length=50, unique=True, null=True)
	mobile = models.PositiveIntegerField(verbose_name='Mobile No', max_length=10, blank=True, null=True)

	class Meta:
		abstract = True


class AbstractAddress(models.Model):
	line_one = models.CharField(verbose_name='Address Line 1', max_length=100, blank=True, null=True)
	line_two = models.CharField(verbose_name='Address Line 2', max_length=100, blank=True, null=True)
	city = models.CharField(verbose_name='City', max_length=30, blank=True, null=True)
	state = models.CharField(verbose_name='State', max_length=30, blank=True, null=True)
	landmark = models.CharField(verbose_name='Landmark', max_length=100, blank=True, null=True)
	locality = models.CharField(verbose_name='Locality', max_length=50, blank=True, null=True)
	pincode = models.PositiveIntegerField(verbose_name='Pin Code', max_length=10, blank=True, null=True)

	class Meta:
		abstract = True


class Customer(AbstractCustomer):
	shipping_address = models.ForeignKey(Address, verbose_name='Shipping Address', blank=True, null=True)
	billing_address = models.ForeignKey(Address, verbose_name='Billing Address', blank=True, null=True)

	class Meta:
		verbose_name = 'Customer'
		verbose_name_plural = 'Customers'


class Address(AbstractAddress):
	customer = models.ForeignKey(Customer, verbose_name='Customer', blank=True, null=True)

	class Meta:
		verbose_name = 'Address'
		verbose_name_plural = 'Addresses'
