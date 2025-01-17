# Generated by Django 4.1.5 on 2024-06-29 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ORDER', '0002_alter_order_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.BooleanField(default=False)),
                ('phone_number', models.IntegerField()),
                ('Title', models.CharField(max_length=50)),
                ('number_of_pages', models.IntegerField()),
                ('deadline', models.DateTimeField()),
                ('abstract', models.FileField(default='null', upload_to='')),
                ('description', models.CharField(default='null', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
