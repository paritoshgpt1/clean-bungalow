from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from service.models import Service
from order.models import *
import datetime

# Create your views here.
def book_service(request):
	context = RequestContext(request)
	services = Service.objects.all().values_list('id', 'service_name')
	if request.method == 'POST':
		print request.POST, request.user, request.user.id, request.user.mobile
		customer_id = request.user.id
		service_id = request.POST.get('service')
		date_value = request.POST.get('date', None)
		start_time_value = request.POST.get('start_time', None)
		stop_time_value = request.POST.get('stop_time', None)
		if date_value is None or date_value == '':
			date_error = "Please enter a date"
			return render_to_response('order/book-service.html', {'services': services, 'date_error': date_error}, context_instance=context)
		if start_time_value is None or start_time_value == '':
			start_time_error = "Please enter a start time"
			return render_to_response('order/book-service.html', {'services': services, 'start_time_error': start_time_error}, context_instance=context)
		if stop_time_value is None or stop_time_value == '':
			end_time_error = "Please enter a end time"
			return render_to_response('order/book-service.html', {'services': services, 'end_time_error': end_time_error}, context_instance=context)
		start_time = datetime.datetime.strptime((date_value + ' ' + start_time_value),'%Y-%m-%d %H:%M')
		stop_time = datetime.datetime.strptime((date_value + ' ' + stop_time_value),'%Y-%m-%d %H:%M')
		service = Service.objects.get(id=service_id)
		order_service, order_service_created = OrderService.objects.get_or_create(service_name=service.service_name)
		order_customer, order_customer_created = OrderCustomer.objects.get_or_create(username=request.user.mobile, defaults = {
			'first_name': request.user.first_name,
			'last_name': request.user.last_name,
			'mobile': request.user.mobile
			})
		Order.objects.create(customer=order_customer, service=order_service, start_time=start_time, stop_time=stop_time)
		return render_to_response('order/book-service-done.html', {}, context_instance=context)
	else:
		return render_to_response('order/book-service.html', {'services': services}, context_instance=context)

