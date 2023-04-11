from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Login(View):
    def get(self, request):
        dt = "Login screen"
        return render(request, "login/login.html")