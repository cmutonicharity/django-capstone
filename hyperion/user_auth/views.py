from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.http import urlencode


# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html', {"redirect": request.GET.get('redirect', '')})


def register(request):
    return render(request, 'authentication/register.html', {"redirect": request.GET.get('redirect', '')})


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            f"{reverse('user_auth:login')}?{urlencode(request.POST['redirect'])}"
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            request.POST['redirect'] or reverse('user_auth:show_user')
        )


def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def complete_registration(request):
    firstname = request.POST['firstname']
    username = request.POST['username']
    password = request.POST['password']
    if User.objects.filter(username=username):
        return render(request, 'authentication/register.html', {
            'error_message': "Username already taken.",
            'redirect': request.POST['redirect']
        })

    user = User.objects.create_user(username, None, password, first_name=firstname)
    user.save()
    login(request, user)

    return HttpResponseRedirect(
        request.POST['redirect'] or reverse('user_auth:show_user')
    )