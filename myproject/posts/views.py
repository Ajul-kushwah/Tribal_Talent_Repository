from django.shortcuts import render,redirect,HttpResponse
from . models import Post,Like,Following
import json
from django.contrib.auth.models import User
from .forms import AddPostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def post_view(request):
    user = Following.objects.get(user=request.user)
    followed_user = [i for i in user.followed.all()]
    followed_user.append(request.user)

    post = Post.objects.filter(author__in = followed_user).order_by('pk')
    # post = Post.objects.all()
    user = request.user
    context ={
        'qs':post,
        'user':user
    }
    return render(request,'posts/main.html',context)

def addPost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # form.save()

            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            author = request.user
            Post(title=title, body=body, author=author).save()
            return redirect('post_list')
        else:
            return redirect('add-post')
    else:
        form = AddPostForm()
        return render(request, 'posts/add_post.html', {'form': form})


def yourPost(request):
    your_post = Post.objects.filter(author = request.user)
    return render(request,'posts/your_post.html',{'your_post':your_post})

def deletePost(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('your-post')

def updatePost(request,id):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        post = Post.objects.get(id=id)
        post.title = title
        post.body=body
        post.author = request.user

        post.save()
        return redirect('your-post')
    else:
        post = Post.objects.get(id=id)
        return render(request, 'posts/update_post.html', {'post':post})


def like_view(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if request.user in post_obj.liked.all():
            post_obj.liked.remove(request.user)
        else:
            post_obj.liked.add(request.user)

        like, created = Like.objects.get_or_create(user=request.user, post_id=post_id)
        print(created)
        if not created:
            if like.value =='Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return redirect('post_list')

def follow(request, username):
    main_user = request.user
    to_follow = User.objects.get(username = username)

    #check if already following
    following = Following.objects.filter(user = main_user, followed = to_follow)
    is_following = True if following else False

    if is_following:
        Following.unfollow(main_user, to_follow)
        is_following = False
    else:
        Following.follow(main_user, to_follow)
        is_following = True

    resp = {
        "following" : is_following,
    }

    response = json.dumps(resp)
    return HttpResponse(response, content_type="application/json")


def liked_post_of_user(request):
    # liked_post = Like.objects.filter(user = request.user,value = 'Like')
    liked_post = Post.objects.filter(liked = request.user)
    # post = Post.objects.get()
    print(liked_post)
    return render(request,'posts/liked_post_of_user.html',{'post':liked_post})

