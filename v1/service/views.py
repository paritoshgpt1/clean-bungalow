from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

# Create your views here.
def ratecard_house(request):
	context = RequestContext(request)
	return render_to_response('service/ratecard-house.html', {}, context_instance=context)

def ratecard_kitchen(request):
	context = RequestContext(request)
	return render_to_response('service/ratecard-kitchen.html', {}, context_instance=context)

def ratecard_bathroom(request):
	context = RequestContext(request)
	return render_to_response('service/ratecard-bathroom.html', {}, context_instance=context)

def ratecard_cooking(request):
	context = RequestContext(request)
	return render_to_response('service/ratecard-cooking.html', {}, context_instance=context)