from django.urls import path
from . import views

app_name = 'second-app'

urlpatterns = [
    path('', views.index, name='users_index'),
    path('users/<str:name>', views.hello_name, name='users_name'),
]