from django import forms
from customer.models import Customer

class RegisterationForm(forms.ModelForm):
	
	#Class for registeration form
	error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        'pssword_incomplete': ("You must confirm your password."), 
    }
  
	first_name=forms.CharField(widget=forms.widget.TextInput,label='First Name')
	last_name=forms.CharField(widget=forms.widget.TextInput, label='Last Name')
	username=forms.CharField(widget=forms.widget.TextInput, label='Username')
	email=forms.EmailField(widget= forms.widget.TextInput, label='Email Id')
	password1=forms.CharField(widget=forms.widget.PasswordInput, label='Password')
	password2=forms.CharField(widget=forms.widget.PasswordInput, label='Confirm Password')

	class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


    def clean_password2(self):
          
        #Verifies that the values entered into the password1 and password2 fields match
        password1 = self.cleaned_data.get('password1')
    	password2 = self.cleaned_data.get('password2')

    	if not password2:
        raise forms.ValidationError(self.error_messages['password_incomplete'], code='password_incomplete',)
    	if password1 != password2:
        	raise forms.ValidationError(
        		self.error_messages['password_mismatch'],
                code='password_mismatch',
        	)
        return password2;

    def save(self, commit=True):
        user = super(RegisterationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user




       
		