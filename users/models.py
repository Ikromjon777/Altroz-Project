from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class CustomUser(AbstractUser):
    img = models.ImageField(upload_to='users/images', default='news/images/iq1.jpg')

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=150)
    subject = models.CharField(max_length=200)
    message = RichTextField()

    def __str__(self):
        return self.subject