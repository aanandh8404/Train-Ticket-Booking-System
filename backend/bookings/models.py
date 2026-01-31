from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Train(models.Model):
    train_no = models.IntegerField(unique=True)
    train_name = models.CharField(max_length=100)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    seats = models.IntegerField()
    fare = models.IntegerField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    total_fare = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=[('BOOKED','Booked'),('CANCELLED','Cancelled')],
        default='BOOKED'
    )
    booked_at = models.DateTimeField(auto_now_add=True)

