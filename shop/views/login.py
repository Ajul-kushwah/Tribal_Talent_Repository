from django.views import View
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from shop.models import User


class LoginView(View):
    return_url = None
    def get(self, request):
        print('From Class BAsed View')
        LoginView.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email, password)
        try:
            user = User.objects.get(email=email)
            flag = check_password(password=password, encoded=user.password)
            if flag:
                # // collect Product
                temp = {}
                temp['email'] = user.email
                temp['id'] = user.id
                request.session['user'] = temp
                if LoginView.return_url:
                    return redirect(LoginView.return_url)
                return redirect('index')
            else:
                return render(request, 'login.html', {'error': 'Email Or Password Invalid'})
        except:
            return render(request, 'login.html', {'error': 'Email Or Password Invalid'})
