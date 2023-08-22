from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Activity(models.Model):
    """
    Activity Model represents an activity that can be booked.

    Attributes
    ----------
    title : CharField
        the short title describing the activity, limited to 200 characters.
    description : TextField
        the full description of the activity.
    price : DecimalField
        the per person price for the activity.
    image : CharField
        the filename of the image to be displayed. Images are stored in static/tour-uploads
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Booking(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_people = models.IntegerField()

    def total(self):
        unit_cost = self.activity.price
        return unit_cost * self.number_of_people
