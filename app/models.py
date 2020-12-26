from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    msg = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.firstname
