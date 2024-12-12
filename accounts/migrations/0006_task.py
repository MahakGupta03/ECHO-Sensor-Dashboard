# Generated by Django 4.2.5 on 2024-12-11 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(max_length=100)),
                ('task_description', models.CharField(max_length=100)),
                ('task_zone', models.IntegerField(max_length=100)),
                ('task_location', models.CharField(max_length=100)),
                ('task_end_date', models.DateField()),
                ('task_end_time', models.TimeField()),
            ],
        ),
    ]