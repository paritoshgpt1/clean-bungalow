from django.db import models

# Create your models here.

class AbstractService(models.Model):
	service_name = models.CharField(verbose_name='Service Name', max_length=30, blank=True, null=True)
	category_fk_category = models.CharField(verbose_name='Category Name', max_length=30, blank=True, null=True)

class AbstractCategory(models.Model):
	category_name = models.CharField(verbose_name='Category Name', max_length=30, blank=True, null=True)


	class Meta:
		abstract = True
    

class Service(AbstractService):
	pass

class Category(AbstractCategory):
	pass

class OrderService(AbstractService):
	pass




