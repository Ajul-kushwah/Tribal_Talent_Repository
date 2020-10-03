from django.urls import path  , re_path
from django.shortcuts import render
from shop.views import index
from shop.views import LoginView, SignupView
from shop.views.email_verification import verifyCode, sendOtp
from shop.views.products import productDetails
from shop.views.download import downloadFree, downloadPaidProduct
from shop.views.payment import createPayment, verifyPayment
from shop.middlewares.login_required_middleware import login_required
from shop.middlewares.can_not_access_after_login import cantAccessAfterLogin
from shop.views.orders import my_orders
from shop.views.reset_password import ResetPassword, PasswordResetVerification, verifyResetPasswordCode
from download_products.settings import  STATIC_URL


urlpatterns = [
    path('', index.index, name='index'),
    path('logout', index.logout, name='logout'),
    path('orders', login_required(my_orders), name='ordes'),

    path('login', cantAccessAfterLogin(LoginView.as_view()), name='login'),
    path('send-otp', cantAccessAfterLogin(sendOtp), name='sendotp'),
    path('verify', cantAccessAfterLogin(verifyCode), name='verify'),

    path('signup', cantAccessAfterLogin(SignupView.as_view()), name='signup'),
    path('product/<int:product_id>', productDetails, name='details'),
    path('download-free/<int:product_id>', downloadFree, name='downloadfree'),

    path('create-payment/<int:product_id>', login_required(createPayment), name='create-payemnt'),
    path('complete-payment', login_required(verifyPayment), name='verify-payemnt'),

    path('download/paidproduct/<int:product_id>', login_required(downloadPaidProduct), name='download-paidproducts'),
    path('reset-password', ResetPassword.as_view(), name='reset-password')
    , path('verify-reset-password-code', verifyResetPasswordCode)
    , path('reset-password-verification', PasswordResetVerification.as_view(), name='reset-password-verfication')


]

print(urlpatterns)
