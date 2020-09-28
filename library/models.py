from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin(models.Model):
	id=models.AutoField(primary_key=True)
	firstname=models.CharField(max_length=66)
	lastname=models.CharField(max_length=66)
	email=models.EmailField(max_length=66)
	username=models.CharField(max_length=66)
	password=models.CharField(max_length=66)




class Book(models.Model):
	bookid=models.AutoField(primary_key=True)
	bookname=models.CharField(max_length=66)
	author=models.CharField(max_length=66)
	category=models.CharField(max_length=66)
	isbn=models.IntegerField()
	

	def __str__(self):
		return self.bookname

	

class Student(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	firstname=models.CharField(max_length=66)
	lastname=models.CharField(max_length=66)
	enrollno=models.CharField(max_length=66)
	branch=models.CharField(max_length=66)

	def __str__(self):
		return self.enrollno


class Issue(models.Model):
	issueid=models.AutoField(primary_key=True)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	enrollno=models.ForeignKey(Student, on_delete=models.CASCADE)
	issuebook=models.ForeignKey(Book,related_name='issuetobook', on_delete=models.CASCADE)
	bookisbn=models.ForeignKey(Book,related_name='isbn_book', on_delete=models.CASCADE)
	issuedate=models.DateField()
	expirydate=models.DateField()

	




