from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def CoC(request):
    return render(request, 'CoC.html', {})