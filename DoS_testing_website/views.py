from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TextForm
from .methods import listFiles, fileIterator, factorial
import os, sys, time as timeLib


def home(request):
    return render(request, "home.html")


######################################################### bandwidth related views
def bwHome(request):
    files = listFiles("./static")

    context = {"files": files, "length": len(files)}

    return render(request, "bw.html", context)


def bw(request, fileName):
    filePath = "./static/" + fileName
    chunkSize = 1024 * 1024

    response = StreamingHttpResponse(fileIterator(filePath, chunkSize))
    response["Content-Length"] = os.path.getsize(filePath)
    response["Content-Type"] = "*/*"
    response["Content-Disposition"] = f'attachment; filename="{fileName}"'

    return response


######################################################### cpu related views


def cpuHome(request):
    num = request.GET.get("text")
    if type(num) != type(None):
        if num.isdigit():
            return redirect(reverse("cpu", args=[num]))
        else:
            return redirect("cpuHome")

    context = {"form": TextForm()}
    return render(request, "cpu.html", context)


def cpu(request, num):
    sys.setrecursionlimit(1000000 + 10)
    sys.set_int_max_str_digits(999999)

    flag = timeLib.time()
    result = factorial(int(num))
    runtime = timeLib.time() - flag

    length = len(str(result))
    form = {"form": TextForm()}

    context = {"result": result, **form, "runtime": runtime, "length": length}
    return render(request, "cpu.html", context)


######################################################### ram related views
def ramHome(request):
    return render(request, "ram.html")
