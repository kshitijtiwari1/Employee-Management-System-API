# Generated by Django 4.1.3 on 2023-02-13 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeemodel',
            options={'ordering': ['employee', 'employee_name', 'work_location', 'date_of_joining']},
        ),
    ]
