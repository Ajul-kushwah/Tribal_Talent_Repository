from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from accounts.models import TribalYouth,Company
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def index(request):
    return render(request,'myapp/index.html')

def indexx(request):
    return render(request,'myapp/contact.html')

from django.core.paginator import Paginator

def all_youth_user(request):
    all_youth=TribalYouth.objects.exclude(username=request.user.username).order_by('-id')
    paginator = Paginator(all_youth,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # context={'account':all_youth}
    context={'account':page_obj}
    #return render(request,'myapp/all_youth_user.html',context)
    return render(request,'myapp/users.html',context)


def all_companies_user(request):
    all_companies=Company.objects.all()
    context={'account':all_companies}
    return render(request,'myapp/companies.html',context)


def user_details(request,id):
    if TribalYouth.objects.filter(user=request.user).exists():
        user_detail=TribalYouth.objects.get(id=id)
        context={'user':user_detail,'company':True}
        return render(request,'myapp/user_details.html',context)

def company_details(request,id):
    company_detail = Company.objects.get(id=id)
    context = {'user': company_detail}
    return render(request, 'myapp/company_details.html', context)


from posts.models import Following
@login_required()
def youth_user_details(request,id):
    youth_user=TribalYouth.objects.get(id=id)
    if TribalYouth.objects.filter(user=request.user).exists():
        user=User.objects.get(username=youth_user.username)
        print(user)
        is_following = Following.objects.filter(user=request.user, followed=user)
        following_obj = Following.objects.get(user=user)
        print(following_obj)
        following,follower = following_obj.follower.count(), following_obj.followed.count()
        context={
            'account':youth_user,
            'following':following,
            'follower':follower,
            'connection':is_following,
            'company':False}
        return render(request,'myapp/youth_user_details.html',context)
    else:
        context = {'account': youth_user, 'company': True}
        return render(request, 'myapp/youth_user_details.html', context)

@login_required()
def company_user_details(request,id):
    company_user=Company.objects.get(id=id)
    if TribalYouth.objects.filter(user=request.user).exists():
        context={'account':company_user,'company':True}
        return render(request,'myapp/company_user_details.html',context)
    else:
        context = {'account': company_user, 'company':False}
        return render(request, 'myapp/company_user_details.html', context)


def upload_profile_photo(request):
    if request.method=='POST':
        profile_image=request.FILES['profile_photo']

        if TribalYouth.objects.filter(user=request.user).exists():
            youth=TribalYouth.objects.get(user=request.user)
            youth.image=profile_image
            youth.save()
            messages.success(request,'profile photo add successfully..')
            return redirect('profile')
        else:
            company=Company.objects.get(user=request.user)
            company.images=profile_image
            company.save()
            messages.success(request, 'profile photo add successfully..')
            return redirect('profile')

    else:
        return render(request,'user/user_profile.html')

def upload_cover_photo(request):
    if request.method=='POST':
        profile_image=request.FILES['cover_photo']

        if TribalYouth.objects.filter(user=request.user).exists():
            youth=TribalYouth.objects.get(user=request.user)
            youth.cover_photo=profile_image
            youth.save()
            messages.success(request, 'cover photo add successfully..')
            return redirect('profile')
        else:
            company=Company.objects.get(user=request.user)
            company.cover_photo=profile_image
            company.save()
            messages.success(request, 'cover photo add successfully..')
            return redirect('profile')
    else:
        return render(request,'user/user_profile.html')

############################################################
def about(request):
    return render(request,'myapp/about.html')


def contact(request):
    return render(request,'myapp/contact.html')