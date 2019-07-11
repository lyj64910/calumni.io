from django.shortcuts import render, redirect, get_object_or_404
from .models import Cal
from django.utils import timezone

# Create your views here.
def home(request):
    cals = Cal.objects.all()
    return render(request,"home.html", {'cals':cals})

def new(request):
    return render(request,'new.html')

def create(request):
    cal = Cal()
    cal.title = request.CAL['cal_title']
    cal.body = request.CAL['cal_body']
    cal.pub_date = timezone.datetime.now()
    cal.save()

    return redirect('home')