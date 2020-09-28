from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('loginadmin/',views.loginadmin,name='loginadmin'),
    path('logoutadmin/', views.logoutadmin, name="logoutadmin"),
    path('loginstudent/',views.loginstudent,name='loginstudent'),
    path('logoutstudent/', views.logoutstudent, name="logoutstudent"),
    path('addbook/',views.AddBook,name='addbook'),
    path('viewbook/',views.ViewBook,name='viewbook'),
    path('addstudent/',views.AddStudent,name='addstudent'),
    path('viewstudent/',views.ViewStudent,name='viewstudent'),
    path('updatebook/<str:pk>',views.UpdateBook,name='updatebook'),
    path('updatestudent/<str:pk>',views.UpdateStudent,name='updatestudent'),
    path('deletebook/<str:pk>',views.DeleteBook,name='deletebook'),
    path('deletestudent/<str:pk>',views.DeleteStudent,name='deletestudent'),
    path('issuebook/',views.IssueNewbook,name='issuebook'),
    path('viewissuebook/',views.ViewIssuebook,name='viewissuebook'),
    path('myissue/<str:pk>',views.MyIssue,name='myissue'),
    path('studenthome/',views.StudentHome,name='studenthome'),
    path('adminhome/',views.AdminHome,name='adminhome'),
    path('updateissue/<str:pk>',views.UpdateIssueBook,name='updateissue'),
    path('deleteissue/<str:pk>',views.DeleteIssueBook,name='deleteissue'),
    

]
