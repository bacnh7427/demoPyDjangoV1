***
Python Django tutorials
***
- Cài đặt Django lên máy:
  - Pip install django
- Tạo project Python trên Pycharm (có thể dùng bản comunity)
- Tạo project django: 
  - django-admin startproject demoform 
- Tạo 1 component trong project django
     python manage.py startapp news     
- Chạy server: bằng 1 trong 2 command dưới
  - python manage.py runserver 
  - python manage.py runserver 127.0.0.1:9000

- Trong quá trình làm:
- Thêm các component nhỏ, và thêm các folder kiểu: templates, static,...
  - Add thêm urls và khai báo thông tin component con trong settings.py của app chính
  - Chỉnh sửa các thứ trong file: views.py, urls.py
    - Views.py là khai báo các hàm xử lý (controller)
    - urls.py (routes)
    - khai báo html có thể tạo thư mục templates/ và vứt trong đấy
- Lệnh migrations DB:
  - python manage.py makemigrations
  - python manage.py migrate
- Create super user:
  - python manage.py createsuperuser
  - Xong thì nhập super user trên admin


- Riêng thằng views.py:
    - Xử lý có thể sử dụng function viết theo thể thức function
    - Hoặc viết class và kế thừa từ class View (xem thêm ở component news)