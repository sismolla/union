# Generated by Django 4.1.5 on 2024-07-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORDER', '0020_transcription_transcribed_file_writhing_editing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcription',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='website_project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='writhing_editing',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
