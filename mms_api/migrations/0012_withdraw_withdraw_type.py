# Generated by Django 4.2.9 on 2024-01-21 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mms_api', '0011_withdrawtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='withdraw_type',
            field=models.ForeignKey(default='f80c3f49-52d3-4cdd-8259-ddc7b5130966', on_delete=django.db.models.deletion.PROTECT, to='mms_api.withdrawtype'),
            preserve_default=False,
        ),
    ]
