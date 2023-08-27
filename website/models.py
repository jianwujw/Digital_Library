from django.db import models

# Create your models here.
#python manage.py makemigrations / migrate
class Book(models.Model):
    title = models.CharField
    author = models.CharField
    date = models.CharField
    image = models.ImageField
    #popularity
    #thumbnail