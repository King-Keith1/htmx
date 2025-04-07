# Generated by Django 5.1.7 on 2025-03-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_tut', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('favorite_framework', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('development_area', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='SampleModel',
        ),
    ]
