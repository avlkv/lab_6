from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from user.models import *
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate


def index(request):
    return render(request, 'base.html')


class EventView(View):
    def get(self, request):
        events = Event.objects.all()
        users = User.objects.all()
        data = {
            'events': events,
            'users': users
        }
        return render(request, 'events.html', data)


class UserView(View):
    def get(self, request):
        users = User.objects.all()
        data = {
            'users': users
        }
        return render(request, 'users.html', data)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        password = request.POST.get('password')
        password_repeat = request.POST.get('password2')
        result = Customers.objects.filter(username=request.POST.get('username')).values()
        list_result = [entry for entry in result]
        if form.is_valid() & (password == password_repeat) & (list_result == []):
            params = {
                'username': request.POST.get("username"),
                'password': request.POST.get("password"),
                'email': request.POST.get("email"),
                'first_name': request.POST.get("first_name"),
                'last_name': request.POST.get("last_name")
            }
            customer = Customers.objects.create(**params)
            customer.save()
            return HttpResponseRedirect('/login/')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


@login_required
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        result = Customers.objects.filter(username=request.POST.get('username'),
                                          password=request.POST.get('password')).values()
        list_result = [entry for entry in result]
        if form.is_valid() & (list_result != []):
            return HttpResponseRedirect('/logout/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
    return render(request, 'logout.html')
