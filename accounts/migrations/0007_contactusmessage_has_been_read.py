# Generated by Django 3.0.4 on 2020-03-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_contactusmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactusmessage',
            name='has_been_read',
            field=models.BooleanField(default=False),
        ),
    ]