# Generated by Django 2.1.3 on 2018-11-21 04:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0005_auto_20181121_0454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('-date_time',)},
        ),
        migrations.AlterField(
            model_name='expense',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 21, 4, 55, 53, 204080, tzinfo=utc)),
        ),
    ]
