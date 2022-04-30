from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    """Table for countries and their codes"""
    fullname = models.CharField(max_length=100)
    code = models.CharField(max_length=4)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class UserAddress(models.Model):
    """Contains user's addresses"""
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50)
    postal_code = models.PositiveIntegerField()
    county = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    telephone = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)

    def __str__(self):
        return self.user_id.username

    class Meta:
        verbose_name = 'User\'s Address'
        verbose_name_plural = 'User\'s Addresses'


class Vendor(User):
    """Model for vendors"""
    biography = models.TextField(blank=True)
    phone = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.company_name or self.username

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"


class Customer(User):
    """Model for regular users"""
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"