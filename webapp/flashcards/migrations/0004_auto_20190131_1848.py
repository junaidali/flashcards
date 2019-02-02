# Generated by Django 2.1.5 on 2019-01-31 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0003_auto_20190116_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_primary', models.CharField(max_length=1024)),
                ('tag_secondary', models.CharField(max_length=1024)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='tags',
            field=models.ManyToManyField(to='flashcards.Tag'),
        ),
    ]