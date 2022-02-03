from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'swarnita'})


def about(request):
    return HttpResponse("this is your about us page.")