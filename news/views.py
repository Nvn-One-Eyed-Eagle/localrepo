from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def home(request):
    all_news = News.objects.all()
    return render (request, "home.html", {"news": all_news, "len": len(all_news)})
def detail_news(request,pk):
    news = News.objects.get(id=pk)
    return render(request,'detail.html', {'news': news})