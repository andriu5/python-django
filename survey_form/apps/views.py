from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def index(request):
    print("2. Imprimiendo desde Metodo index!")
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse('placeholder para mostrar un nuevo formulario para crear un nuevo blog')

def root(request):
    print("1. Imprimiendo desde Metodo root!")
    return redirect('first-app:apps_blogs')

def create(request):
    print("3. Imprimiendo desde Metodo create!")
    return redirect('first-app:apps_create')

def show(request,num):
    number=num
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}")

def renderJson(request,name):
    number={
        'blog_number':10,
        'blog_name':name,
    }
    return render(request, 'blog/index.html', number)

def showJson(request):
    blog={
        'number':1,
        'name':'Ranking de mascotas',
        'location': 'Chile',
        'is_active': True
    }
    return JsonResponse(blog, safe=False)

def edit(request,num):
    number=num
    return HttpResponse(f"placeholder para editar el blog {number}")

def destroy(request,num):
    return redirect('first-app:apps_index')