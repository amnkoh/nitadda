# Generated by Django 3.0.7 on 2020-09-06 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200906_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='lname',
            new_name='last_name',
        ),
    ]
