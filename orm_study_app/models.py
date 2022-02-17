from django.db import models


class User(models.Model):
    email                     = models.CharField(max_length=128, unique=True, null=False, blank=False)
    name                      = models.CharField(max_length=128, null=False, blank=False)
    product_set_included_cart = models.ManyToManyField(to='orm_study_app.Product', related_name='carts_set', 
                                                        through='orm_study_app.Cart',
                                                        through_fields=('related_user', 'related_product'))
    
    class Meta:
        db_table = 'users'


class Seller(models.Model):
    email        = models.CharField(max_length=128, unique=True, null=False, blank=False)
    name         = models.CharField(max_length=128, null=False, blank=False)
    phone_number = models.CharField(max_length=17, unique=True, null=False, blank=False)

    class Meta:
        db_table = 'sellers'


class Product(models.Model):
    name                   = models.CharField(max_length=128, null=False, blank=False)
    price                  = models.PositiveIntegerField(null=False, default=0)
    related_seller         = models.ForeignKey(to='orm_study_app.Seller', on_delete=models.CASCADE, null=False)
    user_set_included_cart = models.ManyToManyField(to='orm_study_app.User', related_name='carts_set', 
                                                        through='orm_study_app.Cart',
                                                        through_fields=('related_product', 'related_user'))

    class Meta:
        db_table = 'products'


class Cart(models.Model):
    related_user    = models.ForeignKey(to='orm_study_app.User', on_delete=models.CASCADE, null=False)
    related_product = models.ForeignKey(to='orm_study_app.Product', on_delete=models.CASCADE, null=False)
    count           = models.PositiveIntegerField(null=False, default=1)

    class Meta:
        db_table = 'carts'

