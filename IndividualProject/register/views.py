from django.http import response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from register.forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    
    return render(request, 'register/register.html', {'form':form})