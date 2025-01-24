from django.db import models

# classes

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    age = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')  # link to image

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # delete user deleting all user's orders
    products = models.ManyToManyField(Product)  #
    date_ordered = models.DateTimeField(auto_now_add=True)
    address_ordered = models.CharField(max_length=200)
    total_price = models.DecimalField(max_digits=11, decimal_places=2)

