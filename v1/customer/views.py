from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.hashers import make_password
from django import forms
from .forms import CustomerForm
from .models import Customer
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from django.core.urlresolvers import reverse


# from customer.forms import LoginForm, RegisterationForm
# Create your views here.


def register(request):
	context = RequestContext(request)
	if request.method == 'POST':
		print request.POST
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		mobile = request.POST.get('mobile')
		name = request.POST.get('name')
		ctx = {}
		error = False
		if password1 != password2:
			ctx.update({'password_error':'Passwords Do Not Match'})
			error = True
		if len(mobile) != 10:
			error = True
			ctx.update({'mobile_error':'Mobile No. should be of 10 digits'})
		if not error:
			password = make_password(password1)
			Customer.objects.create(username=mobile, mobile=mobile, password=password, first_name=name)
			return redirect('/login')
		else:
			return render_to_response('customer/sign-up.html', ctx, context_instance=context)
	else:
		return render_to_response('customer/sign-up.html', {}, context_instance=context)

def home(request):
	context = RequestContext(request)
	return render_to_response('customer/index-old-latest.html', {}, context_instance=context)

def loginUser(request):
	if request.method == 'POST':
		username = request.POST['username'].lower()
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(reverse('order:book_service'))
	else:
		context = RequestContext(request)
		return render_to_response('customer/sign-in.html', {}, context_instance=context)

