from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    search_bar = request.GET.get('searchMovie')
    return render(request, 'home.html', {'search_bar': search_bar})


def about(request):
    return HttpResponse("this is your about us page.")


def signup(request):
    print(request)
    email = request.GET['signupEmail']
    return render(request, 'singup.html', {'email': email})
