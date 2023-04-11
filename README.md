***
<h1>Python Django tutorials</h1>

- Cài đặt Django lên máy:
```
  - Pip install django
```
- Tạo project Python trên Pycharm (có thể dùng bản comunity)
- Tạo project django: 
```
  - django-admin startproject demoform
``` 
- Tạo 1 component trong project django
```
     python manage.py startapp news
```     
- Chạy server: bằng 1 trong 2 command dưới
```
  - python manage.py runserver 
  - python manage.py runserver 127.0.0.1:9000
```
***
- Trong quá trình làm:
- Thêm các component nhỏ, và thêm các folder kiểu: templates, static,...
  - Add thêm urls và khai báo thông tin component con trong settings.py của app chính
  - Chỉnh sửa các thứ trong file: views.py, urls.py
    - Views.py là khai báo các hàm xử lý (controller)
    - urls.py (routes). Lưu ý có urls trong componetn và urls trong source chính
    - khai báo html có thể tạo thư mục templates/ và vứt trong đấy
***
- Lệnh migrations DB:
```
  - python manage.py makemigrations
  - python manage.py migrate
```
- Create super user:
```
  - python manage.py createsuperuser
  - Xong thì nhập super user trên admin
```
- Khai báo trong 
- Xử lý trong file urls.py:

- Riêng thằng views.py:
    - Xử lý có thể sử dụng function viết theo thể thức function
    - Hoặc viết class và kế thừa từ class View (xem thêm ở component news)
***
- Quy trình khởi tạo 1 component: login cho app:
```
- python manage.py startapp login
```
- Trong file settings.py của django app: Thêm dòng khai báo component:
```
  - INSTALLED_APPS = ['login', ]
```
- create 1 file: urls.py
- trong file settings.py của django app: Thêm vào 1 dòng url:
```
    path('login/', include("login.urls")),
```
- trong file views.py của component login: Có thể khai báo view index:
```ssh
     from django.shortcuts import render
     from django.http import HttpResponse
     from django.views import View
     class IndexView(View):
        def get(self, request):
            dt = "Login screen"
            return HttpResponse(dt)
```