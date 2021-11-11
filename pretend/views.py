from django.shortcuts import render
from django.http import HttpResponse


def home_screen_view(request):
    return render(request,"index.html")

def output(request):
    return render(request,"output.html")