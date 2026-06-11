from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Item Name")
    description = models.CharField(max_length=100, verbose_name="Item Description")
    category = models.CharField(max_length=100, choices=[["Veg", "Vegetarian"], ["Non-Veg", "Non-Vegetarian"], ["Vegan", "Vegan"]])
    price = models.IntegerField(default=0, verbose_name="Item Price")
    image_url = models.URLField(verbose_name="image_url")

    def __str__(self):
        return self.name 

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=True)

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Item Quantity")

    @property
    def subtotal(self):
        return self.item.price * self.quantity

    def __str__(self):
        return f"{self.cart.user}'s Cart"