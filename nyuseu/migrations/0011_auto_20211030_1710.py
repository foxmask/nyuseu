# Generated by Django 3.2.8 on 2021-10-30 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyuseu', '0010_myboard_myboardfeeds'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myboard',
            name='short',
        ),
        migrations.RemoveField(
            model_name='myboard',
            name='uuid',
        ),
    ]
