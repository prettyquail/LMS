from .models import Book,Student,Issue,Admin
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.conf import settings



class AdminForm(forms.ModelForm):
	class Meta:
		model=Admin
		fields ='__all__'

class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields ='__all__'

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields ='__all__'


class RegisterForm(UserCreationForm):
	class Meta:
		model=User
		fields =['username','email','password1','password2']

class IssueForm(forms.ModelForm):
	issuedate = forms.DateField(widget=forms.SelectDateWidget())
	expirydate = forms.DateField(widget=forms.SelectDateWidget())
	class Meta:
		model=Issue
		fields ='__all__'