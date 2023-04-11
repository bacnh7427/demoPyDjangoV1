# Class base view
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View


# Create your views here.


class IndexView(View):
    def get(self, request):
        dt = "Notification in scr"
        return HttpResponse(dt)


# class SendData(View):
#     def get(self, request):
#         post_data = PostForm()
#         return render(request, 'news/add_news.html', {'f': post_data})


class ProcessData(View):
    def get(self, request):
        post_data = PostForm()
        return render(request, 'news/add_news.html', {'f': post_data})

    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('Data saved. OK!')
        else:
            return HttpResponse('Data not validate')

    def put(self):
        pass


def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f': b})


def send_email_complete(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            #context2 = {'email': m}
            title = m.cleaned_data['title']
            content = m.cleaned_data['content']
            email = m.cleaned_data['email']
            cc = m.cleaned_data['cc']
            context = {'tt': title, 'ct': content, 'em': email, 'cc': cc}
            return render(request, 'news/email_complete.html', {'email': context})
        else:
            return HttpResponse("Email not valid, sending error. Please check your email")
    else:
        return HttpResponse("Not request post")


# Function base view
# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import PostForm, SendEmail
#
#
# # Create your views here.
#
#
# def index(request):
#     return HttpResponse("Form news")
#
#
# def add_post(request):
#     post_data = PostForm()
#     return render(request, 'news/add_news.html', {'f': post_data})
#
#
# def save_news(request):
#     if request.method == "POST":
#         g = PostForm(request.POST)
#         if g.is_valid():
#             g.save()
#             return HttpResponse('Data saved. OK!')
#         else:
#             return HttpResponse('Data not validate')
#     else:
#         return HttpResponse("Not request post")
#
#
# def email_view(request):
#     b = SendEmail()
#     return render(request, 'news/email.html', {'f': b})
#
#
# def send_email_complete(request):
#     if request.method == "POST":
#         m = SendEmail(request.POST)
#         if m.is_valid():
#             #context2 = {'email': m}
#             title = m.cleaned_data['title']
#             content = m.cleaned_data['content']
#             email = m.cleaned_data['email']
#             cc = m.cleaned_data['cc']
#             context = {'tt': title, 'ct': content, 'em': email, 'cc': cc}
#             return render(request, 'news/email_complete.html', {'email': context})
#         else:
#             return HttpResponse("Email not valid, sending error. Please check your email")
#     else:
#         return HttpResponse("Not request post")