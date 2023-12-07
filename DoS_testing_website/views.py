from django.http import StreamingHttpResponse
from django.shortcuts import render
from .methods import listFiles
import os


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

    def file_iterator(filePath, chunkSize):
        with open(filePath, "rb") as file:
            while True:
                data = file.read(chunkSize)
                if not data:
                    break
                yield data

    response = StreamingHttpResponse(file_iterator(filePath, chunkSize))
    response["Content-Length"] = os.path.getsize(filePath)
    response["Content-Type"] = "*/*"
    response["Content-Disposition"] = f'attachment; filename="{fileName}"'

    return response


######################################################### cpu related views
def cpuHome(request):
    return render(request, "cpu.html")


######################################################### ram related views
def ramHome(request):
    return render(request, "ram.html")
