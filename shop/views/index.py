from django.shortcuts import render, HttpResponse  , redirect
from shop.models import Product, ProductImages , User


def index(request):

    products = Product.objects.filter(active=True)
    print(products)
    data = {
        'products': products
    }
    return render(request, 'index.html', data);


def logout(request):

    request.session.clear()
    return redirect('index')
