from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    myname = "Bac cowell dev"
    mySkill = ["python", "django", 'ruby', "java", "golang"]
    context = {"name": myname, 'skill': mySkill}
    return render(request, "polls/index.html", context)

def getUser(request):
    return HttpResponse("<h1>Get all User vote</h1>")