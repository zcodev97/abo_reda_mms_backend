# Generated by Django 4.2.9 on 2024-02-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mms_api', '0027_deposit_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='deposit_number',
            field=models.PositiveIntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='withdraw_number',
            field=models.PositiveIntegerField(blank=True, unique=True),
        ),
    ]
