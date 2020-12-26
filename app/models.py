from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    msg = models.TextField()
    date = models.DateField()
