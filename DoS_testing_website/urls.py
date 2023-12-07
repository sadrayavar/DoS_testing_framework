from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    #
    path("bw", views.bwHome, name="bwHome"),
    path("bw/<str:fileName>", views.bw, name="bw"),
    #
    path("cpu", views.cpuHome, name="cpuHome"),
    path("cpu/<str:num>", views.cpu, name="cpu"),
    #
    path("ram", views.ramHome, name="ramHome"),
    path("ram/<str:givenTime>", views.ram, name="ram"),
]
