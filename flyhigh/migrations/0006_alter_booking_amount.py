# Generated by Django 4.1.5 on 2023-01-26 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyhigh', '0005_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='amount',
            field=models.IntegerField(),
        ),
    ]