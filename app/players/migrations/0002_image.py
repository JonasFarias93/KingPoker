# Generated by Django 5.1.1 on 2024-10-19 20:35

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
    ]
