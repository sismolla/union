# Generated by Django 4.1.5 on 2024-06-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORDER', '0003_order2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order2',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
    ]
