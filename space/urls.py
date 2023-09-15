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
    path('jobs',views.JobsPageView.as_view(),name='jobs'),
    path('myupdate',views.page_univer),
    path('club',views.ClubView.as_view(),name="club"),
    path('codingclub',views.CodingClubView.as_view(),name="codingclub"),
    path('joinclub',views.JoinCodingClubView.as_view(),name="joincodingclub"),
    path('evsclub',views.ClubView.as_view(),name="club"),
    path('codingcrew',views.CodingCrew.as_view(),name="crews"),
    path('volunteerclub',views.ClubView.as_view(),name="club"),
    path('innovationclub',views.ClubView.as_view(),name="club"),
    path('chatgpt',views.chat_view,name="gpt"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)