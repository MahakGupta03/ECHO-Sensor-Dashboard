
from django.urls import path,include
from accounts.views import *

urlpatterns = [
    path('',register,name="register"),
    path('login/',user_login ,name="login"),
    path('logout/',user_logout ,name="logout"),
    path('dashboard/',dashboard ,name="dashboard"),
    path('city-plan/',show_city_plan ,name="city-plan"),
]