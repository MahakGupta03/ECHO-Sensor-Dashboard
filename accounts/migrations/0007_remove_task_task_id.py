# Generated by Django 4.2.5 on 2024-12-11 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_id',
        ),
    ]