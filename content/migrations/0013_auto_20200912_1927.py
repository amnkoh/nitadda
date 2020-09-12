# Generated by Django 3.0.4 on 2020-09-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_book_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='upload_type',
        ),
        migrations.AddField(
            model_name='book',
            name='upload_type',
            field=models.CharField(choices=[('L', 'Link'), ('P', 'PDF')], default='L', max_length=1),
        ),
    ]