from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Activity, Booking


# Create your views here.
@login_required(redirect_field_name="redirect", login_url=reverse_lazy('user_auth:login'))
def booking_confirm(request):
    """
    Endpoint for creating a new booking of a guided tour.

    Expects to receive an HTTP POST `request`. Creates a new Booking if the passed details are correct.

    :param request: POST request with `activity` and `number_of_people` parameters.
    :return: Redirect to the created booking if successful, otherwise renders the form with the `error_message`
    """
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
    """
    View the details of a booking.

    Will only display the details to the user that created the booking. Other users will
    receive a 404 Not Found error. This is advisable for security reasons rather than returning
    a more meaningful response as it reduces the attack surface.
    :param request: the HTTP request with an authenticated `user`
    :param booking_id: the id of the booking to view
    :return: renders the booking confirmation if found and created by the requester, otherwise 404 Not Found
    """
    user = request.user
    booking = get_object_or_404(Booking, pk=booking_id)
    if booking.user.id != user.id:
        return HttpResponseNotFound("Not Found")
    return render(request, "tourism/booking_confirm.html", {"booking": booking})


def history(request):
    """
    Display history about Rwanda for users interested in visiting.
    :param request: the HTTP request. Does not require authentication.
    :return: renders the history page.
    """
    return render(request, "tourism/history.html")
