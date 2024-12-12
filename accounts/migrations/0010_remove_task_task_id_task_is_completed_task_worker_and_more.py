# Generated by Django 4.2.5 on 2024-12-11 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_id',
        ),
        migrations.AddField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='worker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='accounts.profile'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Completed_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_task_description', models.CharField(max_length=100)),
                ('completed_task_start_date', models.DateField()),
                ('completed_task_start_time', models.TimeField()),
                ('completed_task_end_date', models.DateField()),
                ('completed_task_end_time', models.TimeField()),
                ('original_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='completed_task', to='accounts.task')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed_tasks', to='accounts.profile')),
            ],
        ),
    ]