# Generated by Django 3.0.4 on 2020-03-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_auto_20200325_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='download.jpg', upload_to=''),
        ),
    ]