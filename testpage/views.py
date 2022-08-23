from click import argument
from django.shortcuts import render

# Create your views here.
def index(request):
    
    argumentosget = request.GET.get("nombre") if request.method == "GET" else 0
    # context = {
    #     "a": argumentosget, 
    #     "b": {
    #         "a": 1,
    #         "b": 2
    #         }}
    context = {
        "some_list":["a","b","c"],
        "a":[6,7,8]
        }
    return render(request, "test.html", context)
