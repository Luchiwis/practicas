from click import argument
from django.shortcuts import render

# Create your views here.
def index(request):
    
    argumentosget = request.GET.get("nombre") if request.method == "GET" else 0
    context = {
        "a": argumentosget, 
        "b": {
            "a": 1,
            "b": 2
            }}
    return render(request, "test.html", context)
