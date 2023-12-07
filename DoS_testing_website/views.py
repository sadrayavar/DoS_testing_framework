from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def bwHome(request):
    return render(request, "bw.html")


def cpuHome(request):
    return render(request, "cpu.html")


def ramHome(request):
    return render(request, "ram.html")
