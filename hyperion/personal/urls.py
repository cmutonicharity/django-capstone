from django.urls import path

from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("work/", views.about, name="work"),
    path("fun/", views.about, name="fun"),
]