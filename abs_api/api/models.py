from datetime import datetime
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=80, blank=False)
    phone_number = models.CharField(blank=False, max_length=14, unique=True)
    address = models.CharField(max_length=120, blank=False)
    zone = models.CharField(max_length=25, blank=False)
    zip_code = models.CharField(max_length=9, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=80, blank=False, unique=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'



class Order(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    seller_name = models.ForeignKey(Seller, on_delete=models.CASCADE)
    purchase_date = models.DateField(default=datetime.now())
    delivery_forecast = models.DateField(blank=True, null=True)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    is_paid = models.BooleanField(default=False)
    order_items = models.ForeignKey(OrderItem, on_delete=models.CASCADE)


    @property
    def total_price(self):
        total = sum(self.order_items.total_price_by_product.all())
        return total - self.discount
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    final_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)


    @property
    def product_price(self):
        return self.product.price

    # @property
    # def total_price_by_product(self):
    #     return self.product_price * self.qty
        
    def save(self, *args, **kawrgs):
        self.final_price = self.qty * self.product_price
        super().save(*args, **kawrgs)
        self.order.save()

