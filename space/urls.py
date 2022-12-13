from urllib import request
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('cseclick/',views.cse_view),
    path('ececlick/',views.ece_view),
    path('eeclick/',views.ee_view),
    path('meclick/',views.me_view),
]
