# Generated by Django 2.1.5 on 2019-01-16 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='categories',
            field=models.ManyToManyField(to='flashcards.Category'),
        ),
    ]
