from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from service.models import Service

# Create your views here.
def book_service(request):
	services = Service.objects.all().values_list('id', 'name')
	context = RequestContext(request)
	return render_to_response('order/book-service.html', {'services': services}, context_instance=context)

