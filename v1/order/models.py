from django.db import models
from customer.models import AbstractCustomer, AbstractAddress
from service.models import AbstractService, AbstractCategory
from worker.models import AbstractWorker
from django.db import transaction

class OrderCategory(AbstractCategory):
	pass

	class Meta:
		verbose_name = 'Order Category'
		verbose_name_plural = 'Order Categories'


class OrderService(AbstractService):
	category = models.ForeignKey(OrderCategory, verbose_name='Category', blank=True, null=True)

	class Meta:
		verbose_name = 'Order Service'
		verbose_name_plural = 'Order Services'


class OrderAddress(AbstractAddress):
	pass

	class Meta:
		verbose_name = 'Order Address'
		verbose_name_plural = 'Order Addresses'


class OrderCustomer(AbstractCustomer):
	username = models.CharField(verbose_name='Username', max_length=50, blank=True, null=True)
	shipping_address = models.ForeignKey(OrderAddress, verbose_name='Shipping Address',
										related_name='shipping_customer', blank=True, null=True)
	billing_address = models.ForeignKey(OrderAddress, verbose_name='Billing Address', related_name='billing_customer',
										blank=True, null=True)

	class Meta:
		verbose_name = 'Order Customer'
		verbose_name_plural = 'Order Customers'


class OrderWorker(AbstractWorker):
	service = models.ManyToManyField(OrderService, verbose_name='Services', blank=True)
	# category = models.ForeignKey(OrderCategory, verbose_name='Category', blank=True, null=True)

	class Meta:
		verbose_name = 'Order Worker'
		verbose_name_plural = 'Order Workers'


class Order(models.Model):
	code = models.CharField(verbose_name='Order Code', max_length=50, blank=True, null=True)
	worker = models.ForeignKey(OrderWorker, verbose_name='Order Worker', blank=True, null=True)
	customer = models.ForeignKey(OrderCustomer, verbose_name='Order Customer', blank=True, null=True)
	service = models.ForeignKey(OrderService, verbose_name='Order Service', blank=True, null=True)
	start_time = models.DateTimeField(verbose_name='Start Time', null=True, blank=True)
	stop_time = models.DateTimeField(verbose_name='Stop Time', null=True, blank=True)

	def __str__(self):
		return '%s : %s %s - %s ' % (self.customer.first_name, self.service, self.start_time, self.stop_time)

	@transaction.atomic
	def save(self, *args, **kwargs):
		if not self.code:
			i = Order.objects.values('code')
			if len(i) == 0:
				new_id = 1
			else:
				i = i.latest('code')
				new_id = int(i['code'][2:]) + 1
			self.code = 'CB' + str(format(new_id, '08d'))
		super(Order, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Orders'
