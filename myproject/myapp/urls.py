from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('indexx',views.indexx,name="indexx"),

    path('aaa',views.home,name='home'),
    path('About_Us',views.about,name='about'),
    path('contact',views.contact,name='contact'),

    path('all_youth_user',views.all_youth_user,name='all_youth_user'),
    path('all_companies_user',views.all_companies_user,name='all_companies_user'),



    path('youth_user_details/<int:id>',views.youth_user_details,name='youth_user_details'),
    path('company_user_details/<int:id>',views.company_user_details,name='company_user_details'),

    path('upload_profile_photo',views.upload_profile_photo,name="upload_profile_photo"),
    path('upload_cover_photo',views.upload_cover_photo,name="upload_cover_photo"),
]
