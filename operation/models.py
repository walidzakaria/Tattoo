from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100)
    date = models.DateField()
    artist = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    email = models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
