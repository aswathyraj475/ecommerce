from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateField(auto_now_add=True)

    def subtotal(self):
        return self.quantity*self.product.price


    def __str__(self):
        return self.product.name

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    address=models.TextField()
    phone=models.CharField(max_length=100)
    order_status=models.CharField(max_length=30,default="pending")
    delivery_status=models.CharField(max_length=30,default="pending")
    noofitems=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.noofitems * self.product.price

    def __str__(self):
            return self.user.username

class Account(models.Model):
    acctnumber=models.CharField(max_length=30)
    acctype=models.CharField(max_length=30)
    amount=models.IntegerField()
    def __str__(self):
        return self.acctnumber

