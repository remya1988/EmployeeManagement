# Generated by Django 4.0.6 on 2023-02-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employeeleave_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeleave',
            name='apply_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]