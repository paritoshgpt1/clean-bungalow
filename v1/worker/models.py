from django.db import models

# Create your models here.

class AbstractWorker(models.Model):
	first_name = models.CharField(verbose_name='First Name', max_length=30, blank=True, null=True)
	last_name = models.CharField(verbose_name='Last Name', max_length=30, blank=True, null=True)
	mob_no = models.CharField(verbose_name= 'Mobile No', max_length=50, blank = True, null=True)
	service_mtm_service = models.CharField(verbose_name= 'Services', max_length=50, blank = True, null=True)
	category = models.CharField(verbose_name= 'Category', max_length=50, blank = True, null=True)
	start_time = models.DateTimeField(verbose_name='Start Time', null=True, blank=True)
	end_time = models.DateTimeField(verbose_name='Start Time', null=True, blank=True)

	class Meta:
		abstract = True
    

class Worker(AbstractWorker):
	pass