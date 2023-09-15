from django.urls import path
from .views import eachclub, index, signup,testing,login
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name='index'),
    path('testing',testing,name='testing'),
    path('signup',signup,name='signup'),
    path('login',login,name='login'),
    path('eachclub',eachclub,name='eachclub')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)