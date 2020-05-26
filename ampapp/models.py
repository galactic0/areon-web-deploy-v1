from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    
    message = models.CharField(max_length=32)

    def __str__(self):
        return self.email

class trackingapi(models.Model): 
    distance = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True )
    
    def __str__(self):
        return self.distance
