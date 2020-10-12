from django.shortcuts import render
from accounts.models import TribalYouth,Company


def search_youth_user(request):
    context={}
    if request.method=='GET':
        query=request.GET.get('q')
        query_list=query.split()
        context['query']=query

        youth_user=search_user(query_list)
        if len(youth_user)==0:
            context['empty']=True
        else:
            context['empty']=False
        context['object_list']=youth_user
        return render(request,'search/search_user.html',context)

    else:
        return render(request, 'search/search_user.html', context)


def search_user(query_list):
    users=TribalYouth.objects.all()
    youth=[]
    if len(query_list)==0:
        return users
    else:
        for i in query_list:
            for j in range(len(users)):
                if (i.lower() in users[j].firstname.lower()or i.lower() in users[j].talent_name.lower() ) and users[j] not in youth:
                    youth.append(users[j])
        return youth





def search_company_user(request):
    context={}
    if request.method=='GET':
        query=request.GET.get('qq')
        query_list=query.split()
        context['query']=query

        company_user=search_company(query_list)
        if len(company_user)==0:
            context['empty']=True
        else:
            context['empty']=False
        context['object_list']=company_user
        return render(request,'search/search_company.html',context)

    else:
        return render(request, 'search/search_company.html', context)


def search_company(query_list):
    users=Company.objects.all()
    company=[]
    if len(query_list)==0:
        return users
    else:
        for i in query_list:
            for j in range(len(users)):
                if (i.lower() in users[j].company_name.lower() or i.lower() in users[j].company_type.lower() ) and users[j] not in company:
                    company.append(users[j])
        return company