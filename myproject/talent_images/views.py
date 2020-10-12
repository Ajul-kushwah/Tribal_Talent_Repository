from django.shortcuts import render,redirect
from . models import UserImages,CompanyImages , Skill
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_images(request):
    if request.method=='POST':
        title = request.POST['title']
        image_=request.FILES['image']
        desc = request.POST['description']

        u=UserImages(user=request.user,title=title,image=image_ , desc= desc)
        u.save()
        messages.success(request,"image add successfully...")
        return redirect('all_images')
    else:
        #return render(request,'talent_images/talent_images.html')
        return render(request,'talent_images/images.html')

def company_images(request):
    pass

@login_required()
def all_images(request):
    u_image = UserImages.objects.filter(user = request.user)
    context={'images':u_image}
    return render(request,'talent_images/images.html',context)


def addSkill(request):
    if request.method == 'POST':
        skill = request.POST['skill']
        s = Skill(user=request.user, skill_name = skill)
        s.save()
        messages.success(request,'skill add successfully...')
        return redirect('profile')

    else:
        return render(request,'user/user_profile.html')



def deleteSkill(request,id):
    skill = Skill.objects.get(id=id)
    skill.delete()
    return redirect('profile')


def delete_image(request,id):
    image = UserImages.objects.get(id=id)
    image.delete()
    return redirect('all_images')
