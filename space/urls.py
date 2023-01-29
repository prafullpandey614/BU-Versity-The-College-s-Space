from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index),
    path('previous-year-questions',views.PreviousYearQuestionsView.as_view(),name='pyq'),
    path('notes',views.NotesPageView.as_view(),name='notes'),
    path('university-updates',views.UpdatePageView.as_view(),name='updates'),
    path('myupdate',views.page_univer),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)