from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(OrderCategory)
admin.site.register(OrderService)
admin.site.register(OrderAddress)
admin.site.register(OrderCustomer)
admin.site.register(OrderWorker)
admin.site.register(Order)
