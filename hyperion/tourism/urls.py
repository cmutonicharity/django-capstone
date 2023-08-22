from django.urls import path
from django.views.generic import ListView, DetailView

from . import views
from .models import Activity

app_name = 'tourism'
urlpatterns = [
    path('',
         ListView.as_view(
             queryset=Activity.objects.all(),
             template_name="tourism/tourism.html"
            ),
         name="home"
         ),
    path('activities/<int:pk>/make-booking',
         DetailView.as_view(
             model=Activity,
             template_name="tourism/make_booking.html"
            ),
         name="make-booking"
         ),
    path("activities/confirm-booking", views.booking_confirm, name="booking-confirm"),
    path('bookings/<int:booking_id>', views.view_booking, name="booking"),
    path("history/", views.history, name="history"),
]
