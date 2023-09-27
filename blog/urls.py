from django.urls import path

from . import views


urlpatterns = [
    path('', views.blogs, name='Blog'), 
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'), 

]
