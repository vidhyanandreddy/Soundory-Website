# Generated by Django 3.2.25 on 2025-06-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='movie',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
