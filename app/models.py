from django.db import models

# Create your models here.
class Contact(models.Model):
    id          = models.AutoField(primary_key=True)
    firstname   = models.CharField(max_length=15)
    lastname    = models.CharField(max_length=15)
    email       = models.EmailField()
    phone       = models.CharField(max_length=13)
    msg         = models.TextField()
    date        = models.DateField()
    
    def __str__(self):
        return self.firstname
