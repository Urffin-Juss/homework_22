from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    username = models.CharField( max_length=50, unique=True, verbose_name="username")
    email = models.EmailField(max_length=254, unique=True, verbose_name="email")
    image = models.ImageField(upload_to="users/image", default="images/default.jpg")
    phone_number = PhoneNumberField(max_length=20, unique=True, verbose_name="phone number")
    country = models.CharField(max_length=50, unique=True, verbose_name="country")
    city = models.CharField(max_length=50, unique=True, verbose_name="city")


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email




# Create your models here.
