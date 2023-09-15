import email
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views import View
from .models import NewsUpdates, Notes ,Article,PreviousYearQuestions,ContactMessage,ClubMember
from django.views.generic import ListView ,TemplateView
from .gpt import generate_response
# Create your views here.
def index(request):
    if(request.method=='POST'):
        
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
    template_name = "space/notes.html"
    model = Notes
    context_object_name = "notes"
    def get_queryset(self):
        branch = self.request.GET.get('branch_name')
        sem = self.request.GET.get('semester')
        new_context = Notes.objects.filter(
            branch_name=branch,
            semester  = sem 
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

class JobsPageView(TemplateView):
    template_name = "space/jobs.html"
class ClubView(TemplateView):
    template_name = "space/clubs.html"
    
    
class CodingClubView(TemplateView):
    template_name = "space/codinclub.html"
    
class CodingCrew(TemplateView):
    template_name = "space/coding_crew.html"
      
class JoinCodingClubView(TemplateView):
    template_name = "space/joinclub.html"

    def post(self, request, *args, **kwargs):
        # Retrieve data from the POST request
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        registration_id = request.POST.get('registration_id')
        department = request.POST.get('department')
        availability = request.POST.get('availability')
        level_of_interest = request.POST.get('level_of_interest')
        reason_to_select = request.POST.get('reason_to_select')
        ClubMember.objects.create(name=name, email=email,registration_id=registration_id,department=department,availability=availability,level_of_interest=level_of_interest,reason_to_select=reason_to_select)

        # You can also perform additional logic here if needed

        # Redirect after successful submission (optional)
        return HttpResponseRedirect('')
      

def chat_view(request):
    response = None

    if request.method == "POST":
        user_input = request.POST.get("query", "")
        response = generate_response(user_input)

        return render(request, "space/gpt.html", {"response": response})
    return render(request, "space/gpt.html", {"response": None})
    


def page_univer(request):
    return render(request,"space/university_updates.html")