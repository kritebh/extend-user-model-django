from django.shortcuts import render,HttpResponse
from .models import ExtendUser
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    data = request.user
    return render(request,'core/index.html',{'data':data})