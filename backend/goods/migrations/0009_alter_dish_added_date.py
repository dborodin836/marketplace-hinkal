# Generated by Django 4.0.3 on 2022-03-10 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_alter_dish_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 13, 53, 37, 309972), verbose_name='Added'),
        ),
    ]
