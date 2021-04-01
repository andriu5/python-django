from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
    
# Create your views here.
def index(request):
    return render(request, "users/index.html")

def hello_name(request, name):
    if request.method == "GET":
        context = {
        	"htmlname": name,
        	"namelist": ["Andres", "Eduardo", "Matias"]
        }
        return render(request, "users/index.html", context)
    else:
        return redirect('second-app:users_index')