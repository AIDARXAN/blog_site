# Generated by Django 3.0.5 on 2020-04-11 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200411_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
    ]
