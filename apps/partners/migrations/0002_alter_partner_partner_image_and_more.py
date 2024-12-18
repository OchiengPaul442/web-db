# Generated by Django 4.2.16 on 2024-10-23 18:41

from django.db import migrations
import utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='partner_image',
            field=utils.fields.CustomCloudinaryField(blank=True, default='website/uploads/default_image.webp', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='partner_logo',
            field=utils.fields.CustomCloudinaryField(blank=True, default='website/uploads/default_image.webp', max_length=255, null=True),
        ),
    ]