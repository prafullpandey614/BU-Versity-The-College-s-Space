from django.shortcuts import render
from django.views import View
from models import NewsUpdates
# Create your views here.
def index(request):
    return render(request, 'space/index.html')
class PreviousYearQuestionsView(View):
    template_name = 'space/index.html'
    model = NewsUpdates
    ordering = ["-date_d"]
    context_object_name = "posts"
    def get_queryset(self) :
        data =  super().get_queryset()
        data = data[:3]
        return data