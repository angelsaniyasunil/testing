from django.db import models
# from . import ProductAddingModel

# # Create your models here.

class ProductModel(models.Model):
    profile = models.ImageField(upload_to="Product_image/")
    image = models.ImageField()
    name = models.CharField(max_length=50)
    price = models.FloatField()
    details = models.TextField(max_length=500)

class RegisterModel(models.Model):
    profile = models.ImageField(upload_to="profile_image/")
    full_name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    number = models.IntegerField()
    choose = {
        ("Male","Male"),
        ("Female","Female"),
    }
    gender = models.CharField(max_length=15)
    dob = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=20)