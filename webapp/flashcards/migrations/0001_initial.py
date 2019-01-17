# Generated by Django 2.1.5 on 2019-01-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=512)),
                ('name_ar', models.CharField(max_length=512)),
                ('description_en', models.TextField(max_length=1024)),
                ('description_ar', models.TextField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en', models.CharField(max_length=1024)),
                ('ar', models.CharField(max_length=1024)),
            ],
        ),
    ]