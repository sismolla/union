# Generated by Django 4.1.5 on 2024-06-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORDER', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(editable=False, max_length=5, unique=True),
        ),
    ]
