# Liqpay


    pip install git+https://github.com/liqpay/sdk-python#egg=liqpay
    

NOT this for Python 3 !!!

    pip install liqpay-python
    
  
## Doc

https://www.liqpay.ua/documentation/api/aquiring/checkout/doc


    LIQPAY_PUBLIC_KEY	= '***'
    LIQPAY_PRIVATE_KEY	= '***'

    
URL
    
    path('pay_order/<int:order_id>', pay_order, name="pay_order"),

Link

    <td><a href="{% url 'pay_order' order_id=o.id %}">Pay</a></td>


View

    from liqpay.liqpay3 import LiqPay
    from django.conf import settings
    ...
    
    def pay_order(request,order_id):
        
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        form_html = liqpay.cnb_form({
            'action': 'pay',
            'amount': '10',
            'currency': 'UAH',
            'description': 'pizza description',
            'order_id': 'order_id',
            'version': '3'
        })
        return render(request,'shop/pay_order.html',{'form_html': form_html})
