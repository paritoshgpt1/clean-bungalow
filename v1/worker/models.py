from django.db import models
from service.models import Service, Category


class AbstractWorker(models.Model):
	first_name = models.CharField(verbose_name='First Name', max_length=30, blank=True, null=True)
	last_name = models.CharField(verbose_name='Last Name', max_length=30, blank=True, null=True)
	mobile = models.PositiveIntegerField(verbose_name='Mobile No', max_length=10, blank=True, null=True)
	start_time = models.DateTimeField(verbose_name='Start Time', null=True, blank=True)
	end_time = models.DateTimeField(verbose_name='End Time', null=True, blank=True)

	class Meta:
		abstract = True


class Worker(AbstractWorker):
	service = models.ManyToManyField(Service, verbose_name='Services', blank=True, null=True)
	# category = models.ForeignKey(Category, verbose_name='Category', blank=True, null=True)

	class Meta:
		verbose_name = 'Worker'
		verbose_name_plural = 'Workers'
