from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(default='download.png',null=True,blank=True)


    def __str__(self):
        return self.name



class Products(models.Model):
    CATEGORY = (
        ('phone','Phone'),
        ('sports','Sports'),
    )
    name = models.CharField(max_length=50,null=True,blank=True)
    price = models.FloatField(null=True)
    categori = models.CharField(max_length=20,choices=CATEGORY)
    created_time = models.DateTimeField(auto_now_add=True)
    discription = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('outofdelevery','Out_of_Delevery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    status = models.CharField(max_length=30,null=True,choices=STATUS)
    date = models.DateTimeField(auto_now_add=True)



