# Generated by Django 5.1.1 on 2024-10-19 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_image_public_id_alter_image_image_alter_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
