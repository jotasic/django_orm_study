from django.core.management.base import BaseCommand

from orm_study_app.models        import User, Cart, Seller, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        last_user_id = User.objects.last().id if User.objects.exists() else 0
        User.objects.bulk_create([
                    User(
                         id=last_user_id+i, \
                         email=f'user{last_user_id+i}@django.com', \
                         name=f'유져{last_user_id+i}') \
                         for i in range(1, 11)]
        )

        last_seller_id = Seller.objects.last().id if Seller.objects.exists() else 0
        Seller.objects.bulk_create([
                    Seller(
                            id=last_seller_id+i, \
                            email=f'seller{last_seller_id+i}@django.com', \
                            name=f'판매자{i}', \
                            phone_number=f'010-1234-{last_seller_id+i:0>4}') \
                        for i in range(1, 11)]

        )

        last_product_id = Product.objects.last().id if Product.objects.exists() else 0
        Product.objects.bulk_create([
                    Product(
                         id=last_product_id+i, \
                         name=f'상품{last_product_id+i}', \
                         price = (last_seller_id+i) // 20 * 100, \
                         related_seller_id=last_seller_id+i) \
                         for i in range(1, 11) ]
        )
