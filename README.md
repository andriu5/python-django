Testing Django Project with Multiple Apps
=========================================

# Django Project name: survey_form

The project 'survey_form' have three apps:

* apps
* users
* surveys

# survey_form configuration:

1. survey_form/settings.py
    ```{python}
    INSTALLED_APPS = [
        'apps',
        'users',
        'surveys',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        ]
    ```
2. survey_form/urls.py
    ```{python}
    from django.urls import path, include
    urlpatterns = [
        path('first-app/', include('apps.urls')),
        path('second-app/', include('users.urls')),
        path('third-app/', include('surveys.urls')),
    ]
    ```
# Example of usage in the browser:

## apps:

1. http://127.0.0.1:8000/first-app/blogs-route/        : 127.0.0.1 es la ip donde esta mi localhost
1. http://localhost:8000/first-app/blogs-route/blogs/
1. http://localhost:8000/first-app/blogs-route/new/    :  
1. http://localhost:8000/first-app/blogs-route/create/ : imprime mensajes en la consola
1. http://localhost:8000/first-app/blogs-route/11/
1. http://localhost:8000/first-app/blogs-route/11/edit/
1. http://localhost:8000/first-app/blogs-route/11/delete/
1. http://localhost:8000/first-app/blogs-route/Andres/renderjson/
1. http://localhost:8000/first-app/blogs-route/json/

## users:
1. http://localhost:8000/second-app/
1. http://localhost:8000/second-app/users/Pepito : renderiza una pagina saludando a Pepito y abajo imprime la lista con el nombre de los ususuarios

## surveys:
1. http://localhost:8000/third-app/  : renderiza un formulario, que al hacer POST presionando el boton Submit se renderizan los datos a la pagina result.html agregando la informacion de la session que cuenta las veces que el usuario ha enviado el formulario. Finalmente, se redirecciona a la ruta root de third-app osea a http://localhost:8000/third-app/
