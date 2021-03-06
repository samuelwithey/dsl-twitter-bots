# Generated by Django 3.0.3 on 2020-05-31 12:24

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twittercampaign',
            old_name='upload',
            new_name='dsl_program_upload',
        ),
        migrations.AddField(
            model_name='twittercampaign',
            name='image_upload',
            field=models.ImageField(blank=True, upload_to=core.models.user_directory_path),
        ),
    ]
