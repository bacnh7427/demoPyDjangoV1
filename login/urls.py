from . import views
from django.urls import path
app_name = 'login'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]