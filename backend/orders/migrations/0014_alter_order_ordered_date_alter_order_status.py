# Generated by Django 4.0.3 on 2022-04-27 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_order_modifier_alter_order_ordered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 23, 53, 57, 492409)),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'new order'), ('pending', 'pending order'), ('finished', 'finished order')], default='new', max_length=20),
        ),
    ]
