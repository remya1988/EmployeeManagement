# Generated by Django 4.0.6 on 2023-02-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_email_employee_password_employee_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeleave',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
