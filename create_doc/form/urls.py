from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_document/', views.create_document, name='create_doc'),
]