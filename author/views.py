
from django.shortcuts import render, redirect
from .forms import News
from .forms import NewsForm
# Create your views here.
def news_create(request):
    if request.POST:
        form = News(request.POST, request.POST )
        if form.is_valid():
            form.save()
            return redirect ("home")
        else :
            return render(request, "news_form.html", {"form": form})
    else:
        form = News()
        return render(request, "news_form.html", {"form": form})
