from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CreateUserForm
from offers.models import plans
from offers.forms import PlanForm
from offers.forms import PostpaidForm
from offers.forms import DongleForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
from .serializers import userdetailsSerializer


def index(request):
    records=plans.objects.all()
    postrecords = postpaid.objects.all()
    donglerecords = dongle.objects.all()
    return render(request, "index.html",{'records': records ,'postrecords':postrecords,'donglerecords':donglerecords})
def home(request):
    records = plans.objects.all()
    postrecords = postpaid.objects.all()
    donglerecords = dongle.objects.all()
    return render(request, 'home.html',{'records': records ,'postrecords':postrecords,'donglerecords':donglerecords})

def Adminhome(request):
    records=plans.objects.all()
    postrecords = postpaid.objects.all()
    donglerecords = dongle.objects.all()
    return render(request, 'Adminhome.html',{'records': records ,'postrecords':postrecords,'donglerecords':donglerecords})

def update(request,id):
    context = {}
    obj=get_object_or_404(plans,id=id)
    form=PlanForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/Adminhome')

    context['form']=form
    return render(request,'update.html',context)

def upostpaid(request,id):
    context = {}
    obj=get_object_or_404(postpaid,id=id)
    form=PostpaidForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/Adminhome')

    context['form']=form
    return render(request,'upostpaid.html',context)

def udongle(request,id):
    context = {}
    obj=get_object_or_404(dongle,id=id)
    form=DongleForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/Adminhome')

    context['form']=form
    return render(request,'udongle.html',context)

def delete(request,id):
    res=plans.objects.get(id=id)
    res.delete()
    return redirect('/Adminhome')

def dpostpaid(request,id):
    res=postpaid.objects.get(id=id)
    res.delete()
    return redirect('/Adminhome')

def ddongle(request,id):
    res=dongle.objects.get(id=id)
    res.delete()
    return redirect('/Adminhome')
def  new(request):
    context = {}
    form=PlanForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/Adminhome')

    context['form']=form
    return render(request,'new.html',context)
def npostpaid(request):
    context = {}
    form=PostpaidForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/Adminhome')

    context['form']=form
    return render(request,'npostpaid.html',context)

def ndongle(request):
    context = {}
    form=DongleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/Adminhome')

    context['form']=form
    return render(request,'ndongle.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method =="POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request,'Account was created for' + user)
                return redirect('login')
        context = {'form':form}
        return render(request,'accounts/registration.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user=authenticate(request,username=username, password=password)

            if user is not None:
                return redirect('/home')
            elif username == 'Admin1' and password == 'root12345':
                return redirect('/Adminhome')
            else:
                messages.info(request, 'username OR password is Incorrect')

        context={}
        return  render(request, 'accounts/login.html',context)

def logout(request):
    return redirect('/')



class Userdetailslist(APIView):
    def get(self, request):
        queryset= userdetails.objects.all()
        obj = userdetailsSerializer(queryset, many=True)
        return Response(obj.data)

