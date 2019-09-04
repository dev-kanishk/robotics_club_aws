from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional' )
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def clean_email(self):
    	email = self.cleaned_data['email']
    	if User.objects.filter(email=email).exists():
    		raise forms.ValidationError("Email already exists")
    	return email
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )


class UserProfileForm(forms.ModelForm):
	class Meta():
		model = UserProfile
		fields = ('roll_no','mobile_no','token_got','branch')

