from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=32,null=False)
    description = models.CharField(max_length=2000, null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True,blank=True)
    sold = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    shipping = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(null=False, max_length=32,unique=True)
    description = models.CharField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class CartItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS_CHOICES = [  
        ('Not processed', 'Not processed'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    product = models.ManyToManyField(CartItem)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    adresses =models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not processed')
    updated = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


