from random import choice, randint
from string import ascii_letters
from datetime import datetime
from typing import Sequence

from django.core.management.base import BaseCommand, CommandError

from goods.models import Dish
from user.models import Customer, Vendor, Country
from contact.models import Contact
from orders.models import Discount, Order, OrderItem, OrderModifier

# List for the funcs that will be used to generate data
funcs = []


def generate(func):
    """Decorator that register function that will be used to generate data"""
    funcs.append(func)
    return func


class Command(BaseCommand):
    help = 'Generates random data to populate DB'

    CUSTOMERS_NAME_SAMPLES = (
        'Joe',
        'Jack',
        'Arnold',
        'Alexander',
        'Vladick',
        'Beth',
        'Marta',
        'Bein',
        'Will',
        'Jared',
        'Vladimir',
        'Tony',
        'Julia',
        'Ann',
        'Dan',
        'Dane',
        'Emma',
        'Emanuel',
        'Marcello',
        'Mark',
        'Oliver',
    )

    CUSTOMERS_SURNAME_SAMPLES = (
        'Putin',
        'Beep-Boop',
        'Smith',
        'Leto',
        'Stark',
        'Zinich',
        'Bilik',
        'Schwarzenegger',
        'Macron',
        'Lutz',
        'Pelme',
        'Okken',
        'Kreken',
        'Cramer',
        'Tolkien',
        'Williams',
        'Allen',
        'Mayer',
        'Muller',
        'Scott',
    )

    COMPANY_NAME_SAMPLES = (
        'Mann Co.',
        'MegaHard',
        'Gunix',
        'Stream',
        'Picassa',
    )

    HINKALI_EXTRA = ('Hinkali from ' + country.fullname for country in Country.objects.all())

    DISHES_NAME_SAMPLES = [
        'Borsch',
        'HINKALI',
        'Juice',
        'Pasta',
        'Raviolli',
        'Uzvar',
    ]

    @staticmethod
    def _get_random_date():
        year = randint(2015, 2022)
        month = randint(1, 12)
        day = randint(1, 28)
        hour = randint(0, 23)
        minute = randint(0, 59)
        return datetime(year, month, day, hour, minute)

    @staticmethod
    def _get_username(full_name: str) -> str:
        plain_name = ''.join(full_name.split())
        return plain_name[:randint(6, len(plain_name) - 1)] + '_' + str(randint(1000, 9999))

    @staticmethod
    @generate
    def _create_customers(amount: int = 200,
                          customer_names=None, customer_surnames: Sequence = None, static_password: str = None) -> None:
        names = customer_names or Command.CUSTOMERS_NAME_SAMPLES
        surnames = customer_surnames or Command.CUSTOMERS_SURNAME_SAMPLES
        password = static_password or 'customerpass'

        for _ in range(amount):
            name = choice(names)
            last_name = choice(surnames)
            full_name = name + ' ' + last_name
            username = Command._get_username(full_name)
            email = username + '@email.com'
            try:
                Customer.objects.create(username=username, password=password, email=email, first_name=name,
                                        last_name=last_name, date_joined=Command._get_random_date())
                print(f'User "{username}" created successfully!')
            except Exception as e:
                print('Collision happened!')

    @staticmethod
    @generate
    def _create_vendors(amount: int = 40, customer_names: Sequence = None, customer_surnames: Sequence = None,
                        static_password: str = None) -> None:
        names = customer_names or Command.CUSTOMERS_NAME_SAMPLES
        surnames = customer_surnames or Command.CUSTOMERS_SURNAME_SAMPLES
        password = static_password or 'vendorpass'

        for _ in range(amount):
            name = choice(names)
            last_name = choice(surnames)
            full_name = name + ' ' + last_name
            username = Command._get_username(full_name)
            email = username + '@email.com'
            company = choice(Command.COMPANY_NAME_SAMPLES)
            try:
                Vendor.objects.create(username=username, password=password, email=email, first_name=name,
                                      last_name=last_name, company_name=company, date_joined=Command._get_random_date())
                print(f'User "{username}" created successfully!')
            except Exception as e:
                print('Collision happened!')

    @staticmethod
    @generate
    def _create_dishes(amount: int = 500) -> None:
        for _ in range(amount):
            title = choice(Command.DISHES_NAME_SAMPLES)
            price = randint(100, 1000)
            vendors = Vendor.objects.all()
            rng_vendor = choice(vendors)
            try:
                Dish.objects.create(title=title, description='Blah-blah...',
                                    price=price, added_by=rng_vendor, image='default/not-found.png',
                                    added_date=Command._get_random_date())
                print(f'Dish "{title}" created successfully!')
            except Exception as e:
                print('Collision happened!')

    @staticmethod
    @generate
    def _create_contacts(amount: int = 100) -> None:
        for _ in range(amount):
            name = choice(Command.CUSTOMERS_NAME_SAMPLES)
            sender = name + str(randint(1000, 9999)) + '@mail.com'
            date = Command._get_random_date()
            message = ''.join([choice(ascii_letters + '       ') for _ in range(100)])
            try:
                Contact.objects.create(subject='I NEED HELP, YOU F*CKERS!!!', email=sender,
                                       name=name, added_date=date, message=message)
                print(f'Contact from "{name}" created successfully!')
            except Exception as e:
                print('Collision happened!')

    @staticmethod
    @generate
    def _create_discounts(amount: int = 20) -> None:
        for i in range(amount):
            name = f'Discount ({i})'
            word = ''.join([choice(ascii_letters) for _ in range(50)])
            vendors = Vendor.objects.all()
            rng_vendor = choice(vendors)
            status = choice([True, False])
            discount_amount = randint(5, 30)
            try:
                Discount.objects.create(name=name, description=word, discount_word=word, added_by=rng_vendor,
                                        is_active=status, discount_amount=discount_amount)
                print(f'Discount "{word}" created successfully!')
            except Exception as e:
                print('Collision happened!')

    @staticmethod
    @generate
    def _create_orders(amount: int = 120) -> None:
        for i in range(amount):
            all_discounts = Discount.objects.all()
            all_users = Customer.objects.all()

            status = choice(Order.STATUS)
            discount = choice(all_discounts) if randint(1, 5) == 2 else None
            user = choice(all_users)
            date = Command._get_random_date()
            try:
                order = Order.objects.create(ordered_by=user, comment='Some comment', ordered_date=date,
                                             discount=discount, status=status)
                all_dishes = Dish.objects.all()
                for _ in range(randint(1, 10)):
                    try:
                        dish = choice(all_dishes)
                        amount = randint(1, 10)
                        OrderItem.objects.create(amount=amount, item=dish, order=order)
                    except Exception as e:
                        pass
            except Exception as e:
                print('Collision happened!', e)
            print(f'Order "{order.id}" created successfully!')

    def add_arguments(self, parser):
        ...

    def handle(self, *args, **options):

        def get_success_message(model_name: str) -> str:
            wide = 4 + len(model_name) + len(' created successfully!')
            result = '=' * wide
            result += '= ' + model_name.capitalize() + ' created successfully!' + ' ='
            result += '=' * wide
            return result

        for func in funcs:
            func()
            self.stdout.write(get_success_message(func.__name__.split('_')[-1]))

