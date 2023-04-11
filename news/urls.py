from . import views
from django.urls import path
app_name = 'news'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.SendData.as_view(), name='add_data'),
    path('save/', views.SaveData.as_view(), name='save_data'),
    path('send_email', views.email_view, name='send_email'),
    path('send_email_complete', views.send_email_complete, name='send_email_complete'),

]