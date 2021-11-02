# Generated by Django 3.2.8 on 2021-10-17 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nyuseu', '0009_auto_20211017_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('uuid', models.UUIDField()),
                ('short', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MyBoardFeeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nyuseu.myboard')),
                ('feeds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nyuseu.feeds')),
            ],
        ),
    ]