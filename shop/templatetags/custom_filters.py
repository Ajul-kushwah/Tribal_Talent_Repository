from django import template

register = template.Library();


@register.filter(name='rupee')
def addRupeeSign(value):
    return f'₹ {value}';

@register.filter(name='sale_price')
def getSalePrice(product):
    return ( product.price - ( product.price * (product.discount / 100 ) ) )