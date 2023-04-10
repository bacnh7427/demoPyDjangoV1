from . import views
from django.urls import path
app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_post, name='add_data'),
    path('save/', views.save_news, name='save_data'),
    path('send_email', views.email_view, name='send_email'),
    path('send_email_complete', views.send_email_complete, name='send_email_complete'),

]