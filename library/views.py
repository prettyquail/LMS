from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout,authenticate,login
from .models import Book,Issue,Admin,Student
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import BookForm,StudentForm,IssueForm,AdminForm,RegisterForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext as _
# Create your views here.


def index(request):
	return render(request,'library/index.html')

"""-------------Student-------------------------------------"""
@login_required
def StudentHome(request):
	issue=Issue.objects.all()
	
	return render(request,'library/studenthome.html')

def studentindex(request):
	return render(request,'library/studentindex.html')

def signup(request):
	if request.user.is_authenticated:
		return redirect('studenthome')
	else:
		form = RegisterForm()
		if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('loginstudent')
			

		context = {'form':form}
		return render(request, 'library/signup.html', context)

def loginstudent(request):
	
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request,user)
				return redirect('studenthome')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'library/studentlogin.html', context)



def logoutstudent(request):
	logout(request)
	return redirect('loginstudent')



def MyIssue(request,pk):
	data=Issue.objects.get(issueid=pk)
	return render(request,'library/myissue.html',context={'data':data})



"""--------------------------------Administrator---------------------------"""
def AdminHome(request):
	return render(request,'library/adminhome.html')


def loginadmin(request):
	
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = Admin.objects.filter(username=username, password=password)
			if len(user):
				return render(request,'library/adminhome.html')
			else:
				messages.error(request, "Invalid username or password.")
		context = {}
		return render(request, 'library/adminlogin.html', context)

def logoutadmin(request):
	logout(request)
	return redirect('loginadmin')




def AddBook(request):
	form=BookForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('addbook')
	return render(request,'library/addbook.html',context={'form':form})

def ViewBook(request):
	books=Book.objects.all()
	return render(request,'library/viewbook.html',context={'books':books})

def AddStudent(request):
	form=StudentForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('addstudent')
	return render(request,'library/addstudent.html',context={'form':form})


def ViewStudent(request):
	students=Student.objects.all()
	return render(request,'library/viewstudent.html',context={'students':students})



def UpdateBook(request,pk):
	context={}
	obj=Book.objects.get(bookid=pk)
	form=BookForm(request.POST,instance=obj)
	if form.is_valid():
		form.save()
		messages.success(request, 'Updated Successfully')
		return redirect('viewbook')
	context['form']=form
	return render(request,'library/updatebook.html',context)



def DeleteBook(request,pk):

	obj=Book.objects.get(bookid=pk)
	if request.method=='POST':
		obj.delete()
		return redirect('viewbook')

	return render(request,'library/viewbook.html')



def UpdateStudent(request,pk):
	context={}
	obj=Student.objects.get(user=pk)
	form=StudentForm(request.POST,instance=obj)
	if form.is_valid():
		form.save()
		messages.success(request, 'Updated Successfully')
		return redirect('viewstudent')
	context['form']=form
	return render(request,'library/updatestudent.html',context)



def DeleteStudent(request,pk):

	obj=Student.objects.get(user=pk)
	if request.method=='POST':
		obj.delete()
		return redirect('viewstudent')

	return render(request,'library/viewstudent.html')

def IssueNewbook(request):
	form=IssueForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('viewissuebook')
	return render(request,'library/issuebook.html',context={'form':form})


def ViewIssuebook(request):
	issues=Issue.objects.all()
	return render(request,'library/viewissuebook.html',context={'issues':issues})



def UpdateIssueBook(request,pk):
	context={}
	obj=Issue.objects.get(issueid=pk)
	form=IssueForm(request.POST,instance=obj)
	if form.is_valid():
		form.save()
		messages.success(request, 'Updated Successfully')
		return redirect('viewissuebook')
	context['form']=form
	return render(request,'library/updateissuebook.html',context)



def DeleteIssueBook(request,pk):

	obj=Issue.objects.get(issueid=pk)
	if request.method=='POST':
		obj.delete()
		return redirect('viewissuebook')

	return render(request,'library/viewissuebook.html')
