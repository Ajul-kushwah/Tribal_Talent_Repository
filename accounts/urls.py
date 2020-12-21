from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name="register"),
    path('add-personal-info',views.add_personal_info,name="add-personal-info"),

    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('profile',views.profile,name="profile"),
    path('settings',views.settings_,name="settings"),
    path('delete_account',views.delete_account,name="delete_account"),

    path('edit', views.edit_account, name='edit_account'),

    #path('accounts/add_informations', views.add_informations, name='add_information'),
    #path('accounts/add_company_informations', views.add_company_informations, name='add_company_information'),

    path('change_password',views.change_password,name='change_password'),

    path('delete', views.delete_account, name='delete-account'),
    path('forget', views.forget_password, name='forget'),
    path('reset/<str:token>', views.reset_password, name='reset'),


    path('newpro', views.newpro, name="newpro"),
    path('add_aption', views.addCaption, name="add_aption"),


    path('update_user_info',views.update_user_info,name="update_user_info"),
    path('update_company_info',views.update_company_info,name="update_company_info"),

    path('profile_update', views.profile_update, name="profile_update"),

    path('update_user_contact', views.update_user_contact, name="update_user_contact"),



]
