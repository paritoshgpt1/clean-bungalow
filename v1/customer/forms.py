from django import forms
from .models import Customer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Div, Field, HTML
from django.forms.models import ModelForm

class CustomerForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super(CustomerForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Customer
		fields = ['first_name', 'mobile', 'password']