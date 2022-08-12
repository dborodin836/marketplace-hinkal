# Generated by Django 4.0.4 on 2022-08-12 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("goods", "0021_remove_dish_added_date_category_added_by_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="added_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
