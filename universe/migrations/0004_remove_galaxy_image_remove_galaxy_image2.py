# Generated by Django 4.0.5 on 2022-08-05 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0003_galaxy_image10_galaxy_image11_galaxy_image9'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galaxy',
            name='image',
        ),
        migrations.RemoveField(
            model_name='galaxy',
            name='image2',
        ),
    ]
