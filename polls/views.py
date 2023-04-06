from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    myname = "Bac cowell dev"
    mySkill = ["python", "django", 'ruby', "java", "golang"]
    context = {"name": myname, 'skill': mySkill}
    return render(request, "polls/index.html", context)

def about(request):
    myname = "Bac cowell dev"
    mySkill = ["python", "django", 'ruby', "java", "golang", "rails", "javascript"]
    context = {"name": myname, 'skill': mySkill}
    return render(request, "polls/about.html", context)

def viewlist(request):
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)

def getUser(request):
    return HttpResponse("<h1>Get all User vote</h1>")