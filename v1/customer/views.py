from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect

# from customer.forms import LoginForm, RegisterationForm
# Create your views here.


def register(request):
	context = RequestContext(request)
	return render_to_response('customer/sign-up.html', {}, context_instance=context)

def home(request):
	context = RequestContext(request)
	return render_to_response('customer/index.html', {}, context_instance=context)

def login(request):
	context = RequestContext(request)
	return render_to_response('customer/sign-in.html', {}, context_instance=context)

