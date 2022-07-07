from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from faker import Faker


class Command(BaseCommand):
    help = 'Create username with email and password'

    def add_arguments(self, parser):
        parser.add_argument('amount', choices=range(1, 11), type=int, help='Choose amount of users to create')

    def handle(self, *args, **options):
        fake_method = Faker()
        users_list = []
        amounts = options['amount']
        for i in range(amounts):
            users_list.append(User(
                username=fake_method.user_name(),
                email=fake_method.ascii_free_email(),
                password=make_password(fake_method.password())
            ))
        User.objects.bulk_create(users_list)
        self.stdout.write(self.style.SUCCESS(f'{amounts} users has been created'))
