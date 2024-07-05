
from django.urls import path,include
from accounts.views import *

urlpatterns = [
    path('',register,name="register"),
    path('home/',home,name="home"),
    path('login/',user_login ,name="login"),
    path('logout/',user_logout ,name="logout"),
    path('dashboard/',dashboard ,name="dashboard"),
    path('city-plan/',show_city_plan ,name="city-plan"),
    path('admin-dashboard/',admin_dashboard ,name="admin-dashboard"),
    path('zone-list/',zone_list ,name="zone-list"),
]