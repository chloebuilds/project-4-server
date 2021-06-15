# Generated by Django 3.2.4 on 2021-06-15 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0006_remove_mood_mood_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprintgoal',
            name='end_date',
        ),
        migrations.AddField(
            model_name='mood',
            name='start_date',
            field=models.DateField(default=1),
        ),
        migrations.AddField(
            model_name='sprint',
            name='start_date',
            field=models.DateField(default=1),
        ),
        migrations.AlterField(
            model_name='sprintgoal',
            name='start_date',
            field=models.DateField(default=1),
        ),
    ]