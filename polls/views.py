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

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs":q})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST("choice")
        c = q.choice_set.get(pk=data)
    except:
        HttpResponse("Lỗi khôgn có choice")
    c.vote = c.vote + 1
    c.save()
    return HttpResponse(c.vote)

def getUser(request):
    return HttpResponse("<h1>Get all User vote</h1>")