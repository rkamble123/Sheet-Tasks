# Generated by Django 4.1.5 on 2023-01-06 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='status',
            field=models.IntegerField(choices=[(0, 'Not Started'), (1, 'Started'), (2, 'Working'), (3, 'Done')]),
        ),
    ]