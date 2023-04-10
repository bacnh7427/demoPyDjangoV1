from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.


def index(request):
    return HttpResponse("Form news")


def add_post(request):
    post_data = PostForm()
    return render(request, 'news/add_news.html', {'f': post_data})


def save_news(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('Data saved. OK!')
        else:
            return HttpResponse('Data not validate')
    else:
        return HttpResponse("Not request post")