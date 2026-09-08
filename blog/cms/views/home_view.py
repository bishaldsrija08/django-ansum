from django.shortcuts import render
from urllib import request

def render_home(request):
    return render(request, 'home.html')