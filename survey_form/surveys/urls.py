from django.urls import path, include
from . import views

app_name = 'third-app'

urlpatterns = [ 
    path('', views.index, name='surveys_index'),
    path('process/', views.create_survey, name='surveys_process'),
    path('result/', views.submitted_info, name='surveys_result'),
]