# Generated by Django 4.2.5 on 2024-11-26 13:45

from django.db import migrations
import utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_member_created_member_is_deleted_member_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=utils.fields.CustomCloudinaryField(blank=True, default='website/uploads/default_image.webp', max_length=255, null=True, validators=[utils.fields.validate_image_format, utils.fields.validate_image_format]),
        ),
    ]
