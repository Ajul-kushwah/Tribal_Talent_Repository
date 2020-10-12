from django.urls import path
from . import views

urlpatterns = [

    #path("upload_images",views.upload_images,name="upload_images"),
    path("user_talent_images",views.user_images,name="upload_user_images"),
    path("company_images",views.company_images,name="upload_company_images"),

    path("all_images",views.all_images,name="all_images"),
    path("delete_image/<int:id>",views.delete_image,name="delete_image"),

    path('addSkill',views.addSkill,name = 'add_skill'),
    path('deleteSkill/<int:id>',views.deleteSkill,name = 'delete_skill'),
]