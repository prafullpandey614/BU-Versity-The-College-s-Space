from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Paper,Year,Semester,Branch,Syllabus
# Create your views here.
def index(request):
    return render(request, 'space/index.html')

class PreQuestionView(ListView):
    def get(self,request):
        branch = self.request.GET.get('branch')
        sem = self.request.GET.get('sem')
        year=self.request.GET.get('year')
        data2 = Paper.objects.filter(
            branch__branch=branch,
        sem__sem = sem,
        year__year=year,
        )
        qyear=Year.objects.all()
        qsem=Semester.objects.all()
        qbranch=Branch.objects.all()
        return render(request,'space/prequestion.html',{'data2':data2,'qyear':qyear,'qsem':qsem,'qbranch':qbranch})


class SyllabusView(ListView):
    def get(self,request):
        branch=self.request.GET.get('branch')
        sem=self.request.GET.get('sem')
        data3=Syllabus.objects.filter(
            branch__branch=branch,
            sem__sem=sem,       
        )
        ssem=Semester.objects.all()
        sbranch=Branch.objects.all()
        return render(request,'space/syllabus.html',{'data3':data3,'ssem':ssem,'sbranch':sbranch})