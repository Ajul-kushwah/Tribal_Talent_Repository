from django.shortcuts import render
from django.urls import path
from . import views

# app_name = 'posts'

urlpatterns = [
    path('',views.post_view,name='post_list',),
    path('add_post',views.addPost,name='add-post',),
    path('your_post',views.yourPost,name='your-post',),
    path('delete-post/<int:id>',views.deletePost,name='delete-post',),
    path('update-post/<int:id>',views.updatePost,name='update-post',),
    path('like/',views.like_view,name='like-post',),

    # path('create-post/',views.create_post,name='create-post',),

    path('user/follow/<str:username>', views.follow, name='follow'),
    path('liked_post_of_user/',views.liked_post_of_user,name='liked-post-of-user',),
]
