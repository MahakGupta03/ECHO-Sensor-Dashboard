from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Base.models import BaseModel
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    phone = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    ward = models.IntegerField(max_length=100)
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    
class Task(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="task")
    worker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="tasks")
    # task_id = models.IntegerField(max_length=100)
    task_description = models.CharField(max_length=100)
    task_zone = models.IntegerField(max_length=100)
    task_location = models.CharField(max_length=100)
    task_end_date = models.DateField()
    task_end_time = models.TimeField()
    is_completed = models.BooleanField(default=False)
    solution_photo = models.ImageField(upload_to='solution_photos/', null=True, blank=True)

    def mark_as_completed(self):
        self.is_completed = True
        self.save()
        Completed_Task.objects.create(
            original_task=self,
            worker=self.worker,
            completed_task_description=self.task_description,
            completed_task_start_date=self.task_end_date,
            completed_task_start_time=self.task_end_time,
            completed_task_end_date=self.task_end_date,
            completed_task_end_time=self.task_end_time,
            solution_photo=self.solution_photo
        )

class Completed_Task(models.Model):
    original_task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name="completed_task")
    worker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="completed_tasks")
    completed_task_description = models.CharField(max_length=100)
    completed_task_start_date = models.DateField()
    completed_task_start_time = models.TimeField()
    completed_task_end_date = models.DateField()
    completed_task_end_time = models.TimeField()
    solution_photo = models.ImageField(upload_to='completed_solution_photos/', null=True, blank=True)