# Generated by Django 2.1.3 on 2018-11-21 04:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0002_auto_20181121_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 21, 4, 50, 24, 1591, tzinfo=utc)),
        ),
    ]
