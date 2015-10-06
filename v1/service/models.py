from django.db import models



class AbstractService(models.Model):
	service_name = models.CharField(verbose_name='Service Name', max_length=50, blank=True, null=True)

	class Meta:
		abstract = True


class AbstractCategory(models.Model):
	category_name = models.CharField(verbose_name='Category Name', max_length=30, blank=True, null=True)

	class Meta:
		abstract = True

class Category(AbstractCategory):
	pass

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

class Service(AbstractService):
	category = models.ForeignKey(Category, verbose_name='Category Name', blank=True, null=True)

	class Meta:
		verbose_name = 'Service'
		verbose_name_plural = 'Services'



