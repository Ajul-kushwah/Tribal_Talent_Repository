from django.contrib import admin
from shop.models import ProductImages, Product , User , Payment
from django.utils.html import  format_html

from instamojo_wrapper import Instamojo
from download_products.settings import PAYMENT_API_AUTH_TOKEN , PAYMENT_API_KEY
API = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token= PAYMENT_API_AUTH_TOKEN , endpoint='https://test.instamojo.com/api/1.1/')


# Register your models here.


class ProductImageModel(admin.StackedInline):
    model = ProductImages


class ProductModel(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'get_description' ,
                    'get_price' , 'get_discount', 'get_sale_price' ,  'file' , 'get_thumbnail' ]
    inlines = [ProductImageModel]

    def get_thumbnail(self , obj):
        return format_html(f'''
            <img height='80px' src='{obj.thumbnail.url}'/>
        ''')


    def get_sale_price(self , obj):
        return f'₹ {( (obj.price) - ( obj.price * ( obj.discount /100 )))}'



    def get_description(self , obj):
        return format_html(f'<span title="{obj.description}">{obj.description[0:15]}...</span>')

    def get_price(self , obj):
        return '₹ ' + str(obj.price)

    def get_discount(self , obj):
        return  str(obj.discount) + " %"

    get_sale_price.short_description = "Sale Price"
    get_discount.short_description = "Discount"
    get_price.short_description = "Price"



class UserModel(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'email' , 'phone' , 'active']
    sortable_by = ['id' , 'name']
    list_editable = ['active']

# later

# Payment Model
class PaymentModel(admin.ModelAdmin):
    list_display = ['id' , 'get_user' ,
                    'get_product',
                    'get_status',
                    'amount'
                    ]
    def amount(self , obj):
        return obj.paymentDetails['payment_request']['amount']


    def get_status(self, obj):
        response = API.payment_request_payment_status(
            obj.payment_request_id, obj.payment_id)
        print(response)
        obj.paymentDetails = response
        if obj.status != "Failed":
            return True
        else:
            return False

    def get_user(self , obj):
        return format_html(f'<a target="_blank" href="/admin/shop/user/{obj.user.id}">{obj.user}</a>')

    def get_product(self , obj):
        return format_html(f'<a target="_blank" href="/admin/shop/product/{obj.product.id}">{obj.product}</a>')

    get_user.short_description = 'User'
    get_product.short_description = 'Product'

    get_status.short_description = 'Status'
    get_status.boolean = True


admin.site.register(Product , ProductModel)
admin.site.register(User , UserModel)
admin.site.register(Payment , PaymentModel)

