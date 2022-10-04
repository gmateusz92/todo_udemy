from . import views
from django.urls import path

urlpatterns = [
    path('', views.signup, name='signup'),
    path('current', views.currenttodos, name='currenttodos'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('home', views.home, name='home'),
    path('login', views.loginuser, name='loginuser'),
    path('create', views.createtodo, name='createtodo'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
    path('completed', views.completedtodos, name='completedtodos'),
    ]
