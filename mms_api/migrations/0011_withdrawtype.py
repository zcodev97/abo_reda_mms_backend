# Generated by Django 4.2.9 on 2024-01-21 19:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mms_api', '0010_alter_company_title_alter_container_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
