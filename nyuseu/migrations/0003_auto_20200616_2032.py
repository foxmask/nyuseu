# Generated by Django 3.0.7 on 2020-06-16 18:32

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('nyuseu', '0002_auto_20200615_2244'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='articles',
            managers=[
                ('unreads', django.db.models.manager.Manager()),
            ],
        ),
    ]
