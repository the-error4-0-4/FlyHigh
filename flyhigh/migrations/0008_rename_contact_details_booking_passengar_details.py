# Generated by Django 4.1.5 on 2023-01-27 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flyhigh', '0007_remove_booking_f_name_remove_booking_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='contact_details',
            new_name='passengar_details',
        ),
    ]