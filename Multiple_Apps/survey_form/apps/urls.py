from django.urls import path, include
from . import views

app_name = 'first-app'

urlpatterns = [ path('blogs-route/', include([
    path('', views.root, name='apps_index'),
    path('blogs/', views.index, name='apps_blogs'),
    path('new/', views.new, name='apps_new'),
    path('create/', views.create, name='apps_create'),
    path('<int:num>/', views.show , name='apps_num'),
    path('<int:num>/edit/', views.edit, name='apps_num_edit'),
    path('<int:num>/delete/', views.destroy, name='apps_delete'),
    path('<str:name>/renderjson/', views.renderJson, name='apps_renderJson'),
    path('json/', views.showJson, name='apps_showJson')
])),
]