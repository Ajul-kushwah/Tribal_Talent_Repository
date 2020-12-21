from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.models import TribalYouth,Company
from .models import ChatApp
from django.db.models import Q
import operator

from django.http import HttpResponse
# Create your views here.


@login_required
def send_message(request, un):
    if request.method == 'POST':
        message = request.POST['message']
        if TribalYouth.objects.filter(username=request.user.username).exists():
            receiver = Company.objects.get(company_username=un)
        else:
            receiver = TribalYouth.objects.get(username=un)

        chat = ChatApp(sender=request.user.username, receiver=un, message=message)
        chat.save()
        return redirect('view-message', un)
    else:
        data={'un':un}
        #return render(request,'chat/view_message.html',data)
        return render(request,'chat/mesage.html',data)


@login_required
def view_user(request):

    if TribalYouth.objects.filter(username=request.user.username).exists():
        company = Company.objects.all()
        data = {'company': True}
    else:
        company = TribalYouth.objects.all()
        data = {'company': False}
    data['users'] = company
    return render(request, 'chat/view_user.html', data)


@login_required
def view_message(request, un):
    if TribalYouth.objects.filter(username=request.user.username).exists():
        account = Company.objects.get(company_username=un)
        userm = TribalYouth.objects.get(username=request.user.username)
    else:
        account = Company.objects.get(company_username=request.user.username)
        userm = TribalYouth.objects.get(username=un)
    message = (Q(sender=userm.username) & Q(receiver=account.company_username)) | (Q(sender=account.company_username) & Q(receiver=userm.username))
    chat = ChatApp.objects.filter(message)
    chat = sorted(chat, key=operator.attrgetter('date'))
    data = {'chats': chat, 'id': un, 'acc': request.user.username}
    print('msg =',message)
    #return HttpResponse('hello',data)
    #return render(request, 'chat/view_message.html', data)
    return render(request, 'chat/mesages.html', data)

