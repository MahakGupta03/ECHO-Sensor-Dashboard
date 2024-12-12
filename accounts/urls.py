
from django.urls import path,include
from accounts.views import register, home, user_login, user_logout, dashboard, worker_dashboard, show_city_plan, supervisor_dashboard, zone_list, assign_task_to_worker, mark_task_as_completed

urlpatterns = [
    path('',register,name="register"),
    path('home/',home,name="home"),
    path('login/',user_login ,name="login"),
    path('logout/',user_logout ,name="logout"),
    path('dashboard/',dashboard ,name="dashboard"),
    path('worker-dashboard/',worker_dashboard ,name="worker-dashboard"),
    path('city-plan/',show_city_plan ,name="city-plan"),
    path('supervisor-dashboard/',supervisor_dashboard ,name="supervisor-dashboard"),
    path('assign-task/<int:worker_id>', assign_task_to_worker,name="assign-task"),
    path('mark_task_completed/', mark_task_as_completed, name='mark_task_as_completed'),
    # path('assign-task-form/<int:user_id>',assign_task_form ,name="assign-task-form"),
    path('zone-list/',zone_list ,name="zone-list"),
]