from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Activity, Booking


# Create your views here.
@login_required(redirect_field_name="redirect", login_url=reverse_lazy('user_auth:login'))
def booking_confirm(request):
    user = request.user
    activity_id = request.POST['activity']
    number_of_people = request.POST['number_of_people']
    activity = get_object_or_404(Activity, pk=activity_id)
    if not number_of_people.isnumeric() or int(number_of_people) > 12 or int(number_of_people) < 1:
        return render(request, "tourism/make_booking.html", {
            'activity': activity,
            'error_message': "Please specify the number of people you are booking for, between 1 and 12"
        })
    booking = Booking(activity=activity, user=user, number_of_people=number_of_people)
    booking.save()
    return HttpResponseRedirect(
        reverse('tourism:booking', args=(booking.id,))
    )


@login_required(redirect_field_name="redirect", login_url=reverse_lazy('user_auth:login'))
def view_booking(request, booking_id):
    user = request.user
    booking = get_object_or_404(Booking, pk=booking_id)
    if booking.user.id != user.id:
        return HttpResponseNotFound("Not Found")
    return render(request, "tourism/booking_confirm.html", {"booking": booking})


def history(request):
    return render(request, "tourism/history.html")
