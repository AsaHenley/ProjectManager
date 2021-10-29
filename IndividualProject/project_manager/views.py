from django.shortcuts import render

def home(request):
    return render(request, 'project_manager/home.html', {})
