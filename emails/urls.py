from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('/home',views.home, name="home"),
    path('/user-dashboard',views.sent_threshold_mail,name="user-dashboard")
]