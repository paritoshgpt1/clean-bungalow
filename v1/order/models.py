from django.db import models
from customer.models import AbstractCustomer, AbstractAddress
from service.models import AbstractService, AbstractCategory
from worker.models import AbstractWorker


class Order(models.Model):
	code = models.CharField(verbose_name='Order Code', max_length=50, blank=True, null=True)
	worker = models.ForeignKey(OrderWorker, verbose_name='Order Worker', blank=True, null=True)
	customer = models.ForeignKey(OrderCustomer, verbose_name='Order Customer', blank=True, null=True)
	service = models.ForeignKey(OrderService, verbose_name='Order Service', blank=True, null=True)
	start_time = models.DateTimeField(verbose_name='Start Time', null=True, blank=True)
	stop_time = models.DateTimeField(verbose_name='Stop Time', null=True, blank=True)

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Orders'


class OrderService(AbstractService):
	category = models.ForeignKey(OrderCategory, verbose_name='Category Name', blank=True, null=True)

	class Meta:
		verbose_name = 'Order Service'
		verbose_name_plural = 'Order Services'


class OrderCustomer(AbstractCustomer):
	shipping_address = models.ForeignKey(OrderAddress, verbose_name='Shipping Address', blank=True, null=True)
	billing_address = models.ForeignKey(OrderAddress, verbose_name='Billing Address', blank=True, null=True)

	class Meta:
		verbose_name = 'Order Customer'
		verbose_name_plural = 'Order Customers'


class OrderAddress(AbstractAddress):
	pass

	class Meta:
		verbose_name = 'Order Address'
		verbose_name_plural = 'Order Addresses'


class OrderCategory(AbstractCategory):
	pass

	class Meta:
		verbose_name = 'Order Category'
		verbose_name_plural = 'Order Categories'


class OrderWorker(AbstractWorker):
	service = models.ManyToManyField(OrderService, verbose_name='Services', blank=True, null=True)
	# category = models.ForeignKey(OrderCategory, verbose_name='Category', blank=True, null=True)

	class Meta:
		verbose_name = 'Order Worker'
		verbose_name_plural = 'Order Workers'
