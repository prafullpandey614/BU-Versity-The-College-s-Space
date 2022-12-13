from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index),
<<<<<<< HEAD
    path('previous-year-questions',views.PreviousYearQuestionsView.as_view(), name='pyq'),
    path('notes',views.NotesPageView.as_view(),name='notes'),
    path('our-team',views.OurTeamView.as_view(),name='our-team'),
   
=======
    path('previous-year-questions',views.PreviousYearQuestionsView.as_view()),
    path('notes',views.NotesPageView.as_view(),name='notes'),
    path('university-updates',views.UpdatePageView.as_view(),name='updates'),
>>>>>>> a05e8fef204af0f4a54ef349eaaf41719d2c3fc5
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)