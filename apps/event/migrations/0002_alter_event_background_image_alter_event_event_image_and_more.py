# Generated by Django 4.2.16 on 2024-10-21 09:32

import utils.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='background_image',
            field=utils.fields.CustomCloudinaryField(
                blank=True, default='website/uploads/default_image.webp', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=utils.fields.CustomCloudinaryField(
                blank=True, default='website/uploads/default_image.webp', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='partnerlogo',
            name='partner_logo',
            field=utils.fields.CustomCloudinaryField(
                blank=True, default='website/uploads/default_image.webp', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource',
            field=utils.fields.CustomCloudinaryField(
                blank=True, default='website/uploads/default_image.webp', max_length=255, null=True),
        ),
    ]
