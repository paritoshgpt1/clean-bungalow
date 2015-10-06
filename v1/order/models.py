from django.db import models

# Create your models here.

class AbstractOrder(models.Model):
	worker_name = models.CharField(verbose_name='Worker Name', max_length=30, blank=True, null=True)
	mob_no = models.CharField(verbose_name= 'Mobile No', max_length=50, blank = True, null=True)
	service_mtm_service = models.CharField(verbose_name= 'Services', max_length=50, blank = True, null=True)
	category = models.CharField(verbose_name= 'Category', max_length=50, blank = True, null=True)
	service_fk_oder_service = models.CharField(verbose_name='Service Order', max_length=30, blank=True, null=True)
	start_time = models.DateTimeField(verbose_name='Start Time', null=True, blank=True)
	stop_time = models.DateTimeField(verbose_name='Stop Time', null=True, blank=True)

	class Meta:
		abstract = True
    

class Order(AbstractOrder):
	pass


		