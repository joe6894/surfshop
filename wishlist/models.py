from django.db import models
from products.models import Product
from profiles.models import UserProfile


class UserWishlist(models.Model):
    user_profile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, null=False, blank=False)
    wished_products = models.ManyToManyField(
        Product, related_name='userwishlists')

    def __str__(self):
        return '{} Wishlist'.format(self.user_profile.user.username)
