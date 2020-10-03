from unittest.mock import _patch

from django.shortcuts import render, HttpResponse  , redirect
from shop.models import Product, ProductImages , User , Payment
from instamojo_wrapper import Instamojo
from download_products.settings import PAYMENT_API_AUTH_TOKEN , PAYMENT_API_KEY
API = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token= PAYMENT_API_AUTH_TOKEN , endpoint='https://test.instamojo.com/api/1.1/')

import math

def createPayment(request , product_id):

    user = request.session.get('user')
    print(user)
    product = Product.objects.get(id= product_id)
    userObject = User.objects.get(id=user.get('id'))
    amount = (product.price - ( product.price *(product.discount /100) ) )
    response = API.payment_request_create(
        amount= math.floor(amount),
        purpose= f'Payment For {product.name}',
        send_email=True,
        buyer_name= userObject.name,
        email= user.get('email'),
        redirect_url="http://52.66.114.119/complete-payment"
    )
    print(response)
    # print the long URL of the payment request.
    payment_request_id = response['payment_request']['id']

    payment = Payment(user=User(id = user.get('id') ) ,
                      product=product ,
                      payment_request_id = payment_request_id )
    payment.save()

    url = response['payment_request']['longurl']
    print(response)
    return redirect(url)








def verifyPayment(request):
    payment_id = request.GET.get('payment_id')
    payment_request_id = request.GET.get('payment_request_id')
    response = API.payment_request_payment_status(
        payment_request_id, payment_id)

    print(response)

    status = response['payment_request']['payment']['status']
    if status != "Failed":
        payment = Payment.objects.get(payment_request_id = payment_request_id)
        payment.payment_id = response['payment_request']['payment']['payment_id']
        payment.status = status
        payment.save()

        return render(request , "download_product_after_payment.html" , {"payment" : payment})
    else:
        return render(request , 'payment_fail.html')


