from store.models.members import Members
from store.models.categories import Category
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from .models.club_socities import ClubSociety
from .models.categories import Category
# Create your views here.

def testing(request):
    Club_Society=None
    Club=None
    name=request.GET.get('club')
    category=Category.get_all_category()
    categoryId=request.GET.get('id')
    if categoryId :
        Club=ClubSociety.get_by_name(name)
        Club_Society=ClubSociety.get_all_clubsociety_by_id(categoryId)
    else:
        Club=ClubSociety.get_by_name(name)
        Club_Society=ClubSociety.get_all_ClubSociety()
    data={}
    data['club_society']=Club_Society
    data['category']=category
    data['club']=Club
    return render(request,'testing.html',data)

def index(request):
    print(request.user)
    return render(request,'index.html')

def validateMember(member):

    if member.isExist():
            errormessage="Email Address Already Registered"

def registerMember(request):
        errormessage=None
        reqPost=request.POST
        firstname=reqPost.get('firstname')
        lastname=reqPost.get('lastname')
        mobile=reqPost.get('mobile')
        email=reqPost.get('email')
        password=reqPost.get('password')

        values={
            'firstname':firstname,
            'lastname':lastname,
            'mobile':mobile,
            'email':email
        }

        member=Members(firstname=firstname,
                            lastname=lastname,
                            mobile=mobile,
                            email=email,
                            password=password)

        errormessage=validateMember(member)

        if not errormessage:
            member.register()
            return redirect('testing')
        else:
            data={
                'error':errormessage,
                'value':values
            }
            return render(request,'signup.html',data)


def signup(request):
    if request.method=="GET":
       return render(request,'signup.html')
    else:
        return registerMember(request)
    
def login(request):
    if request.method =='GET':
        return render(request,'index.html')
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        return HttpResponse("POST")

def eachclub(request):
    print(request.user)
    if (request.user.is_authenticated):
        Club=None
        name=request.GET.get('club')
        Club=ClubSociety.get_by_name(name)
        return render(request,'eachclub.html',{'clubs':Club})
    return redirect('index.html')