from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TribalYouth,Company,Token
from talent_images.models import Skill


from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

first_time_login = 0
def demo_login(request):
    user = auth.authenticate(username='demo',password='demo')
    if user is not None:
        auth.login(request,user)
        return redirect('/')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user =auth.authenticate(username=username,password=password)
        print('user value=',user)
        if user is not None:
            auth.login(request,user)
            # if first_time_login :
            #     print(first_time_login)
            #     return redirect('settings')
            if request.session.get('new') == 'yes':
                print('yes')
                return redirect('settings')
            else:
                request.session['new'] = 'no'
                print('new=',request.session.get('new'))
                return redirect('/')
        else:
            messages.error(request,'Invalid username & password')
           # messages.info(request,'Invalid username and password')
            return redirect('login')
    else:
        return render(request,'accounts/login-register.html')

def register(request):

    if request.method=='POST':
        #first_name=request.POST['first_name']
        #last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email']
        category=request.POST['category']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist ..')
                print('username already exist ..')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist..')
                print('email already exist..')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                print('user created ')
                if category=='youth-user':
                    youth = TribalYouth(user=user,username=username,email=email,category=category)
                    youth.save()
                    messages.success(request,'Register successfully')
                    request.session['new']='yes'
                    print('new = ',request.session.get('new'))
                    return redirect('login')

                    #d={'d':username}
                    #return render(request,'accounts/personal-info.html',d)
                else:
                    company=Company(user=user,company_username=username,company_email=email,category=category)
                    company.save()
                    messages.success(request, 'Register successfully')
                    return redirect('login')
        else:
            print('password not matching...')
            messages.error(request, 'password not matching ..')
            return redirect('register')

    else:
        return render(request,'accounts/login-register.html')



def add_personal_info(request):
    return render(request,'accounts/personal-info.html')


def logout(request):
    auth.logout(request)
    #return redirect('home')
    return redirect('/')

@login_required
def profile(request):

    if TribalYouth.objects.filter(username=request.user.username).exists():
        account = TribalYouth.objects.get(user=request.user)
        user_skill = Skill.objects.filter(user = request.user)
        context = {'account': account,'skill':user_skill}
        #return render(request,'accounts/youth_profile.html',context)
        return render(request,'user/user_profile.html',context)
    else:
        #return HttpResponse('company')
        account = Company.objects.get(user=request.user)
        context = {'account': account}
        return render(request, 'company/company_profile.html', context)

def settings_(request):

    if TribalYouth.objects.filter(username=request.user.username).exists():
        account = TribalYouth.objects.get(user=request.user)
        # user_skill = Skill.objects.filter(user = request.user)
        context = {'account': account}
        #return render(request,'accounts/youth_profile.html',context)
        return render(request,'user/settings.html',context)
    else:
        #return HttpResponse('company')
        account = Company.objects.get(user=request.user)
        context = {'account': account}
        return render(request, 'company/settings.html', context)


def edit_account(request):
    if TribalYouth.objects.filter(username=request.user.username).exists():
        if request.method == 'POST':
            username = request.POST['username']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']

            account = User.objects.get(username=request.user.username)

            account.first_name = firstname
            account.last_name = lastname
            account.username = username
            account.email = email
            account.save()

            TribalYouth(username=username,firstname=firstname,lastname=lastname,email=email).save()
            messages.success(request,'your information successfully update')
            return redirect('profile')

        else:
            return render(request,'accounts/user_profile_update.html')

    else:
        if request.method == 'POST':
            username = request.POST['username']
            firstname = request.POST['firstname']
            email = request.POST['email']

            account = User.objects.get(username=request.user.username)

            account.first_name = firstname
            account.username = username
            account.email = email
            account.save()

            comp=Company.objects.get(user=request.user)
            comp.company_username=username
            comp.company_name=firstname
            comp.company_email=email
            comp.save()
            messages.success(request, 'your information successfully update')
            return redirect('profile')

        else:
            #account = User.objects.get(id=request.user.id)
            #context = {'account': account}
            #return render(request, 'accounts/edit_account.html', context)
            return render(request, 'accounts/company_profile_update.html')


def update_user_info(request):
    if request.method=='POST':
        father_name=request.POST['father_name']
        father_mobile_no=request.POST['father mobile no.']
        your_age=request.POST['your age']
        your_mobile_no=request.POST['your mobile no.']
        area=request.POST['area']
        city=request.POST['city']
        city_pincode=request.POST['city pincode']


        experience=request.POST['experience']
        language=request.POST['language']

        youth=TribalYouth.objects.get(user=request.user)

        youth.father_name=father_name
        youth.father_mobile_no=father_mobile_no
        youth.age=your_age
        youth.your_mobile_no=your_mobile_no
        youth.area=area
        youth.city=city
        youth.city_pincode=city_pincode

        youth.experience=experience
        youth.language=language

        youth.save()
        messages.success(request, 'your information successfully add..')
        return redirect('profile')
    else:
        return render(request,'user/user_profile_update.html')


def update_company_info(request):
    if request.method=='POST':
        registration_no=request.POST['registration_no']
        trending_name=request.POST['trending_name']
        type=request.POST['company_type']

        establishment=request.POST['establishment']
        landline=request.POST['landline_no']
        fax=request.POST['fax_no']
        no_of_employee=request.POST['no_of_employee']
        #status=request.POST['company_status']
        # category=request.POST['category']

        #country=request.POST['country']
        #state=request.POST['state']
        city=request.POST['city']
        city_pincode=request.POST['city_pincode']
        website=request.POST['website']
        image = request.FILES['area']

        company=Company.objects.get(user=request.user)

        company.registration_no=registration_no
        company.company_trending_name=trending_name
        company.company_type=type
        #company.category=category
        #company.company_status=status
        company.establishment_year=establishment
        company.no_of_employee=no_of_employee

        company.landline_no=landline
        company.fax_no=fax
        company.city = city
        company.city_pincode = city_pincode

        company.website=website
        company.images=image

        company.save()
        messages.success(request, 'your information successfully add...')
        return redirect('profile')

    else:
        return render(request,'company/company_profile_update.html')


from .forms import AddCaptionForm
def addCaption(request):
    if request.method == 'POST':
        form = AddCaptionForm(request.POST)
        if form.is_valid():
            caption = form.cleaned_data['caption']
            youth = TribalYouth.objects.get(user=request.user)
            youth.caption=caption
            youth.save()
            return redirect('profile')
        else:
            return redirect('profile_update')
    # else:
    #     form = AddCaptionForm()
    #     return render(request, 'posts/add_post.html', {'form': form})

# def add_informations(request):
#     #user = User.objects.get(pk=pk)
#     youth = TribalYouth.objects.get(user=request.user)
#     context = {'account':youth}
#     if request.method == 'POST':
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         age = request.POST['age']
#         high_qualifications = request.POST['highestqualification']
#         city = request.POST['city']
#
#         youth.firstname = firstname
#         youth.lastname = lastname
#         youth.age = age
#         youth.highqualification = high_qualifications
#         youth.city=city
#         youth.save()
#         return redirect('profile')
#
#     else:
#         return render(request, 'accounts/add_youth_information.html', context)

# def add_company_informations(request):
#     company = Company.objects.get(user=request.user)
#     context = {'account': company}
#
#     if request.method=='POST':
#         cname=request.POST['name']
#         ctype=request.POST['type']
#         clocation=request.POST['location']
#         cdesc=request.POST['company_desc']
#
#         company.company_name=cname
#         company.company_type=ctype
#         company.location=clocation
#         company.company_desc=cdesc
#
#         company.save()
#         return redirect('profile')
#     else:
#         return render(request,'accounts/add_company_information.html',context)
#


@login_required
def change_password(request):
    if request.method=='POST':
        old_password=request.POST['old-password']
        new_password=request.POST['new-password']
        confirm_password=request.POST['confirm-password']
        user=auth.authenticate(username=request.user.username,password=old_password)
        if user==request.user:
            if new_password==confirm_password:
                user.set_password(new_password)
                user.save()
                return redirect('logout')
            else:
                messages.error(request, 'password not match')
                return redirect('change_password')
        else:
            messages.error(request,'wrong password')
            return redirect('change_password')
    else:
        #return render(request,'accounts/change_password.html')
        if TribalYouth.objects.filter(user=request.user).exists():
            return render(request,'user/user_profile_update.html')
        else:
            return render(request,'company/company_profile_update.html')


def delete_account(request):
    user = request.user
    user.delete()
    return redirect('/')

import string
import random
def token_generator():
    size = 20
    chars = string.ascii_lowercase+string.digits
    token = "".join(random.choice(chars) for x in range(size))
    try:
        tok = Token.objects.get(token=token)
        token_generator()
    except:
        return token


def forget_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            token = token_generator()
            tok = Token(token=token, user=user)
            tok.save()
            subject = "Reset Password"
            message = "Reset Your password by click the below link\n http://localhost:8000/accounts/reset/"+str(token)
            from_mail = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject,message,from_mail,to_list)
            return redirect('login')
        else:
            messages.error(request,"You are not registered")
            return redirect("register")
    else:
        return render(request, 'accounts/forget_password.html')


def reset_password(request, token):
    if Token.objects.filter(token=token).exists():
        if request.method == 'POST':
            password = request.POST['password']
            password2 = request.POST['password2']
            if password == password2:
                tok = Token.objects.get(token=token)
                user = tok.user
                user.set_password(password)
                user.save()
                tok.delete()
                messages.success(request, "Your password has been successfully reset")
                return redirect("login")
            else:
                messages.error(request, "password does not match")
                return redirect("reset")
        else:
            return render(request, "accounts/reset_password.html")
    else:
        messages.error(request, "Invalid Token")
        return redirect("login")


def update_user_contact(request):
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        website = request.POST['website']

        c = TribalYouth.objects.get(user=request.user)
        c.email = email
        c.your_mobile_no = phone
        c.website = website

        c.save()
        return redirect('profile')
    else:
        return render(request,'user/user_profile.html')


def newpro(request):
    return render(request,'account/profile.html')









@login_required
def profile_update(request):

    if TribalYouth.objects.filter(username=request.user.username).exists():
        account = TribalYouth.objects.get(user=request.user)
        context = {'account': account,'form':AddCaptionForm(instance=request.user)}
        return render(request,'user/user_profile_update.html',context)

    else:
        account = Company.objects.get(user=request.user)
        context = {'account': account}
        return render(request, 'company/company_profile_update.html', context)

def delete_account(request):
    request.user.delete()
    return HttpResponse('delete')
