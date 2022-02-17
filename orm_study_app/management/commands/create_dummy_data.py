from django.core.management.base import BaseCommand

from orm_study_app.models        import User, Cart, Seller, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        last_id = User.objects.last().id if User.objects.exists() else 0

        User.objects.bulk_create([
                    User(email=f'user{i}', \
                         name=f'유져{i}') \
                         for i in range(last_id, last_id+100) ]

        )
