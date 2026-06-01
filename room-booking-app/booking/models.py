from django.db import models
from datetime import date

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector_availability = models.BooleanField(default=False)

    @property
    def is_booked_today(self):
        return self.bookings.filter(date=date.today()).exists()
class Booking(models.Model):
    date = models.DateField()
    comment = models.TextField(blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')

    class Meta:
        unique_together = ('date', 'room')