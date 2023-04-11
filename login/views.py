from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate


class Login(View):

    def get(self, request):
        dt = "Login screen"
        return render(request, "login/login.html")

    def post(self, request):
        tendangnhap = request.POST.get('username')
        matkhau = request.POST.get('password')
        user_login = authenticate(username = tendangnhap, password = matkhau)
        if user_login is None:
            return HttpResponse('User khong ton tai')
        return HttpResponse("Ban vua bam dang nhap %s %s" %(tendangnhap, matkhau))