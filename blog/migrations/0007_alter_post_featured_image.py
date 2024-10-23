# Generated by Django 4.2.16 on 2024-10-23 09:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_image_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
