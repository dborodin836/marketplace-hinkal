# Generated by Django 4.0.3 on 2022-04-28 00:53

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True,
                                                  on_delete=django.db.models.deletion.CASCADE,
                                                  parent_link=True, primary_key=True,
                                                  serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True,
                                                  on_delete=django.db.models.deletion.CASCADE,
                                                  parent_link=True, primary_key=True,
                                                  serialize=False, to=settings.AUTH_USER_MODEL)),
                ('biography', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=100)),
                ('company_name', models.CharField(default='', max_length=50)),
            ],
            options={
                'verbose_name': 'Vendor',
                'verbose_name_plural': 'Vendors',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.PositiveIntegerField()),
                ('telephone', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('county',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                   to='user.country')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                                 to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "User's Address",
                'verbose_name_plural': "User's Addresses",
            },
        ),
    ]
