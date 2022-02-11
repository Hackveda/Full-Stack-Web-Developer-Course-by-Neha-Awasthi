from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def home(request):
    search_bar = request.GET.get('searchMovie')
    if search_bar:
        query_set = Movie.objects.filter(title__icontains=search_bar)
    else:
        query_set = Movie.objects.all()
    return render(request, 'home.html', {'search_bar': search_bar,'movie':query_set})


def about(request):
    return HttpResponse("this is your about us page.")


def signup(request):
    print(request)
    email = request.GET['signupEmail']
    return render(request, 'singup.html', {'email': email})
