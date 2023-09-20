from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def home(request):
    requested_url = request.path[1:3]
    if requested_url == "":
        return render(request, "myapp/index.html")
    elif requested_url == "fa":
        return render(request, "myapp/indexfa.html")
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')