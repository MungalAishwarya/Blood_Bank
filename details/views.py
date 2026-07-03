from django.shortcuts import render
from django.http import HttpResponse
from .models import Blood


# Create your views here.

def home(request):
    return render(request,'home.html')

def welcome(request):
    return render(request,'welcome.html')

def register(request):
    if request.method == 'POST':
        ID=request.POST.get('ID')
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        age=int(request.POST.get('age'))
        phoneno=request.POST.get('phoneno')
        BGroup=request.POST.get('BGroup')
        state=request.POST.get('state')
        city=request.POST.get('city')
        password = request.POST.get('password')
        b1=Blood(ID=ID,name=name,gender=gender,age=age,phoneno=phoneno,BGroup=BGroup,state=state,city=city,password=password)
        b1.save()
        return render(request,'login.html',{'msg':'Record Inserted'})
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        if Blood.objects.filter(name=username,password=password).exists():
            return render(request,'welcome.html',{'username':username})
        else:
            return HttpResponse("User can't Login")

    else:
        return render(request, 'login.html')


def search(request):
    if request.method == 'POST':
        BGroup = request.POST.get('BGroup')

        if Blood.objects.filter(BGroup=BGroup).exists():
            res = Blood.objects.filter(BGroup=BGroup)
        else:
            res = None

        return render(request, 'search.html', {'d1': res})

    return render(request, 'search.html')


def logout(request):
    return render(request, 'home.html')