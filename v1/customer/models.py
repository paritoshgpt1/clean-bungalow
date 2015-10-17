from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AnonymousUser, Group
from django.utils import timezone

class CustomerManager(BaseUserManager):

	def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
		now = timezone.now()
		if not username:
			raise ValueError('The given username must be set')

		user = self.model(username=username, mobile=username, is_staff=is_staff, is_superuser=is_superuser, last_login=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
		
	def create_user(self, username, password, **extra_fields):
		user = self._create_user(username, password, False, False, **extra_fields)
		return user

	def create_superuser(self, username, password, **extra_fields):
		user = self._create_user(username, password, True, True, **extra_fields)
		group, created = Group.objects.get_or_create(name='Administrator')
		user.groups.add(group)
		user.save()
		return user

	def get_queryset(self):
		return super(CustomerManager, self).get_queryset().all()

class AbstractCustomer(AbstractBaseUser):
	first_name = models.CharField(verbose_name='First Name', max_length=30, blank=True, null=True)
	last_name = models.CharField(verbose_name='Last Name', max_length=30, blank=True, null=True)
	email = models.EmailField(verbose_name="Email", max_length=50, unique=True, null=True, blank=True)
	mobile = models.CharField(verbose_name='Mobile No', blank=True, null=True, max_length=10)
	
	is_active = models.BooleanField(verbose_name='Is Active', default=True)
	is_staff = models.BooleanField(verbose_name='Is Super user', default=False)
	is_admin = models.BooleanField(default=False)

	def __str__(self):
		return '%s %s' % (self.id, self.username)

	def get_full_name(self):
		return '%s %s' % (self.first_name, self.last_name)

	def get_group(self):
		return '%s' % self.group

	def get_username(self):
		return '%s' % self.username

	def get_short_name(self):
		return self.first_name

	class Meta:
		abstract = True


class AbstractAddress(models.Model):
	line_one = models.CharField(verbose_name='Address Line 1', max_length=100, blank=True, null=True)
	line_two = models.CharField(verbose_name='Address Line 2', max_length=100, blank=True, null=True)
	city = models.CharField(verbose_name='City', max_length=30, blank=True, null=True)
	state = models.CharField(verbose_name='State', max_length=30, blank=True, null=True)
	landmark = models.CharField(verbose_name='Landmark', max_length=100, blank=True, null=True)
	locality = models.CharField(verbose_name='Locality', max_length=50, blank=True, null=True)
	pincode = models.PositiveIntegerField(verbose_name='Pin Code', blank=True, null=True)

	class Meta:
		abstract = True


class Address(AbstractAddress):
	customer = models.ForeignKey('Customer', verbose_name='Customer', blank=True, null=True)

	class Meta:
		verbose_name = 'Address'
		verbose_name_plural = 'Addresses'


class Customer(AbstractCustomer, PermissionsMixin):
	username = models.CharField(verbose_name='Username', max_length=50, blank=True, null=True, unique=True)
	shipping_address = models.ForeignKey(Address, verbose_name='Shipping Address', related_name='shipping_customer',
										blank=True, null=True)
	billing_address = models.ForeignKey(Address, verbose_name='Billing Address', related_name='billing_customer',
										blank=True, null=True)

	USERNAME_FIELD = 'username'

	objects = CustomerManager()

	class Meta:
		verbose_name = 'Customer'
		verbose_name_plural = 'Customers'
