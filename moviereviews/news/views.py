from django.shortcuts import render

# Create your views here.
from .models import News


def news(request):
    news_object = News.objects.all()
    return render(request, 'news.html', {'news_object': news_object})
