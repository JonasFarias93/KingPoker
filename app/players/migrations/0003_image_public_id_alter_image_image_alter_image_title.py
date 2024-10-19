# Generated by Django 5.1.1 on 2024-10-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='public_id',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
