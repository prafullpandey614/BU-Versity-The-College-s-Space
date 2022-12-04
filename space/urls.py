from urllib import request
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('previous-year-papers', views.pyq)
]
