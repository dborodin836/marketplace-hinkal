# Generated by Django 4.0.3 on 2022-04-27 20:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_vendor_name_vendor_biography'),
        ('orders', '0010_alter_order_ordered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.vendor'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 23, 16, 19, 658770)),
        ),
    ]
