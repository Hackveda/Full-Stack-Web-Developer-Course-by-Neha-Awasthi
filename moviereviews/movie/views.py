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
    name = 'Neha'
    contact_number = '8054946672'
    email = 'nawasthi34@gmail.com'
    return render(request, 'about_us.html', {'name': name, 'contact': contact_number,'email':email})


def signup(request):
    print(request)
    email = request.GET['signupEmail']
    return render(request, 'singup.html', {'email': email})
