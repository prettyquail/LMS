from django.contrib import admin
from .models import Book,Issue,Admin,Student
# Register your models here.
admin.site.register(Book)
admin.site.register(Issue)
admin.site.register(Admin)
admin.site.register(Student)
