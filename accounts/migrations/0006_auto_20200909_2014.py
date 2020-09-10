# Generated by Django 3.0.7 on 2020-09-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200908_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='registration_number',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active'),
        ),
    ]