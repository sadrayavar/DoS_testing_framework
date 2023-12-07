from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def bwHome(request):
    return HttpResponse("bwHome")


def cpuHome(request):
    return HttpResponse("cpuHome")


def ramHome(request):
    return HttpResponse("ramHome")