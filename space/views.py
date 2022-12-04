from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'space/home.html')


# All Department Index Link
def cse_view(request):
    return render(request,'space/cse/index.html')

def ece_view(request):
    return render(request,'space/ece/index.html')

def ee_view(request):
    return render(request,'space/ee/index.html')

def me_view(request):
    return render(request,'space/me/index.html')

    