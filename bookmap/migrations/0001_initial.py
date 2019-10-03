# Generated by Django 2.2.5 on 2019-09-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('addr', models.TextField(unique=True)),
                ('site', models.URLField(default='홈페이지가 없습니다.')),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]