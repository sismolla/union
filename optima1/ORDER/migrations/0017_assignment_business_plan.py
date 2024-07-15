# Generated by Django 4.1.5 on 2024-06-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORDER', '0016_transcription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('title', models.CharField(default='not given', max_length=200)),
                ('number_of_pages', models.IntegerField()),
                ('deadline', models.DateTimeField(max_length=100)),
                ('abstract', models.FileField(upload_to='assignment/')),
                ('description', models.TextField()),
                ('accept_terms', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Business_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('title', models.CharField(default='not given', max_length=200)),
                ('number_of_pages', models.IntegerField()),
                ('deadline', models.DateTimeField(max_length=100)),
                ('abstract', models.FileField(upload_to='business_plan/')),
                ('description', models.TextField()),
                ('accept_terms', models.BooleanField(default=True)),
            ],
        ),
    ]
