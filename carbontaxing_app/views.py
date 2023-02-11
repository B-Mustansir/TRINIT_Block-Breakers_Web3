from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    companies = carbonEmmited.objects.all()
    context = {}
    context['companies'] = companies
    return render(request,"index.html",context)

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already used")
                return redirect('/')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('/')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('/')
        else:
            messages.info(request,'password is not same')
            return redirect('sign-up')
    else:
        return render(request,"sign-up.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if username=="admin" and user is not None:
            auth.login(request,user)
            return redirect('/govDashboard')
        elif user is not None:
            auth.login(request,user)
            return redirect('/company_dashboard')
        else:
            messages.info(request,'credentials invalid')
            return redirect('sign-in')
    else:
        return render(request,'sign-in.html')
    
def company_dash(request):
    if request.method=='POST':
        company_name = request.user
        sector=request.POST['sector']
        carbonEmmitedCO2=request.POST['carbonemittedByCO2']
        carbonEmmitedCH4=request.POST['carbonemittedByCH4']
        carbonEmmitedN2O=request.POST['carbonemittedByN2O']
        carbonEmmitedF=request.POST['carbonemittedByFluorine']
        carbonEmmitedTotal=request.POST['carbonemitted']
        year=request.POST['year']
        public_key=request.POST['publickey']
        emmit = carbonEmmited(company_name=company_name,carbon_emmited_CO2=carbonEmmitedCO2,carbon_emmited_CH4=carbonEmmitedCH4,carbon_emmited_N2O=carbonEmmitedN2O,carbon_emmited_F=carbonEmmitedF,carbon_emmited_Total=carbonEmmitedTotal,year=year,public_key=public_key)
        emmit.save()
        return HttpResponse("Form Submitted")
    else:return render(request,"dashboard.html")
    

def gov_dash(request):
    if request.method=='POST':
        sector_name = request.POST['sector']
        capalloted=request.POST['cap']
        capping = carbonCap(sector_name=sector_name,cap_alloted=capalloted)
        carbonCap.save()
        return render(request,"govDashboard.html")
    else:return render(request,"govDashboard.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

# def signUp(request):
#     return render(request, "sign-up.html")

def signIn(request):
    return render(request, "sign-in.html")

def dashboard(request):
    return render(request,"dashboard.html")

def dash_form(request):
    company_name = request.user
    sector=request.POST['sector']
    carbonEmmitedCO2=request.POST['carbonemittedByCO2']
    carbonEmmitedCH4=request.POST['carbonemittedByCH4']
    carbonEmmitedN2O=request.POST['carbonemittedByN2O']
    carbonEmmitedF=request.POST['carbonemittedByFluorine']
    carbonEmmitedTotal=request.POST['carbonemitted']
    year=request.POST['year']
    public_key=request.POST['publickey']
    emmit = carbonEmmited(company_name=company_name,carbon_emmited_CO2=carbonEmmitedCO2,carbon_emmited_CH4=carbonEmmitedCH4,carbon_emmited_N2O=carbonEmmitedN2O,carbon_emmited_F=carbonEmmitedF,carbon_emmited_Total=carbonEmmitedTotal,year=year,public_key=public_key)
    emmit.save()
    return render(request,"dashboard.html")