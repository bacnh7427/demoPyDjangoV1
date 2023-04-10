from . import views
from django.urls import path
app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_post, name='add_data'),
    path('save/', views.save_news, name='save_data')

]