import email
from django.shortcuts import render
from django.views import View
from .models import NewsUpdates, Notes,PreviousYearQuestions,ContactMessage
from django.views.generic import ListView , TemplateView
# Create your views here.
def index(request):
    if(request.method=='POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email,message=msg)
        return render(request, 'space/index.html',{"message":"yes"})
    return render(request, 'space/index.html',{"message":"no"})
class PreviousYearQuestionsView(ListView):
    template_name = 'space/pyq.html'
    model = PreviousYearQuestions
    
    context_object_name = "papers"
    def get_queryset(self):
        branch = self.request.GET.get('branch_name')
        sem = self.request.GET.get('semester')
        year = self.request.GET.get('year')
        new_context = PreviousYearQuestions.objects.filter(
            branch_name=branch,
            semester = sem,
            year = year,
        )
        return new_context

class NotesPageView(ListView):
    template_name = "space/Notes_page.html"
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
class OurTeamView(TemplateView):
    template_name = "space/OurTeamPage.html"

    # def get_context_data(self, **kwargs):
    #     context = super(NotesPageView, self).get_context_data(**kwargs)
    #     context['branch'] = self.request.GET.get('branch')
    #     context['semester'] = self.request.GET.get('semester', 'give-default-value')
    #     return context