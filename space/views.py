from django.shortcuts import render
from django.views import View
from .models import NewsUpdates, Notes ,Article
from django.views.generic import ListView 
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
    def get(request, *args, **kwargs):
        pass
    def post(request, *args, **kwargs):
        pass

class NotesPageView(ListView):
    template_name = "blog/index.html"
    model = Notes
    # ordering = ["-date_d"]
    context_object_name = "notes"
    def get_queryset(self):
        branch = self.request.GET.get('branch_name')
        sem = self.request.GET.get('semester')
        new_context = Notes.objects.filter(
            branch_name=branch,
            semester = sem,
        )
        return new_context
# def update_page(request):
# def get_context_data(self, **kwargs):
    #     context = super(NotesPageView, self).get_context_data(**kwargs)
    #     context['branch'] = self.request.GET.get('branch')
    #     context['semester'] = self.request.GET.get('semester', 'give-default-value')
    #     return context
class UpdatePageView(View):
    model = Article
    template_name = 'space/university_updates.html'
    context_object_name = "articles"
        
    