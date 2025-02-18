from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_total_sum(self):
        return sum(item.number * item.product.price for item in self.items.all())



    def __str__(self):
        return f"Cart of {self.user.username}"



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=1)


    def get_total_price(self):
        return self.number * self.product.price

    def __str__(self):
        return f"{self.number} of {self.product.name}"