# Generated by Django 5.1.7 on 2025-05-31 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrailApp', '0005_alter_task_taskstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskstatus',
            field=models.IntegerField(choices=[(0, 'Not Started'), (1, 'In Progress'), (2, 'Completed')], default=0),
        ),
    ]
