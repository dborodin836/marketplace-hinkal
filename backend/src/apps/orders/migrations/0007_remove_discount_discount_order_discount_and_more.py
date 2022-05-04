# Generated by Django 4.0.4 on 2022-05-04 09:07

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0006_remove_order_discount_discount_discount_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="discount",
            name="discount",
        ),
        migrations.AddField(
            model_name="order",
            name="discount",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="orders.discount",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="ordered_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 5, 4, 12, 7, 34, 658527)
            ),
        ),
    ]