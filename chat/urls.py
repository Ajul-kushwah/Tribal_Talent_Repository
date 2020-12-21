from django.urls import path
from . import views

urlpatterns = [
    path('all_user', views.view_user, name='view-user'),
    path('all_user/<str:un>', views.view_message, name='view-message'),
    path('all_user/send/<str:un>', views.send_message, name='send-message'),
]