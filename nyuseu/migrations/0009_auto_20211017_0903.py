# Generated by Django 3.2.8 on 2021-10-17 07:03

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('nyuseu', '0008_articles_unique_article'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='feeds',
            managers=[
                ('feeds', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='feeds',
            name='multiboard',
            field=models.BooleanField(default=True),
        ),
    ]
