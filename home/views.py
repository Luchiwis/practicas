from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "a": request.GET.get("nombre"), 
        "b": {
            "a": 1,
            "b": 2
            }}
    return render(request, "home.html", context)
