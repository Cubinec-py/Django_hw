from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Delete username by id'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int)

    def handle(self, *args, **options):
        users_id = options['user_id']
        superuser = User.objects.filter(is_superuser=True).values_list('id', flat=True).order_by('id')
        if set(users_id).intersection(set(superuser)):
            self.stdout.write(self.style.ERROR('Superuser cannot be deleted!'))
        else:
            deleter = User.objects.filter(id__in=users_id).delete()
            self.stdout.write(self.style.SUCCESS(f'{deleter} users has been deleted'))
