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

    class Meta:
        app_label = 'tourism'


class Booking(models.Model):
    """
    Booking Model represents a Booking made of an `activity` by a `user`.

    Attributes
    ----------
    activity : Activity
        The activity booked by the `user`
    user : User
        The user who made the booking
    number_of_people : IntegerField
        The number of people booked for
    """
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_people = models.IntegerField()

    def total(self):
        """
        Gets the total cost of the booking

        The total cost is based on the `activity.price` and `number_of_people`
        :return: the total price of the booking
        """
        unit_cost = self.activity.price
        return unit_cost * self.number_of_people

    class Meta:
        app_label = 'tourism'
