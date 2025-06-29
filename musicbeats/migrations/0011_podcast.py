# Generated by Django 3.2.25 on 2025-06-28 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0010_liked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('audio', models.FileField(upload_to='songs/')),
                ('creator', models.CharField(max_length=50)),
            ],
        ),
    ]
