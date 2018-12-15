# Session

If you don’t want to use sessions, you might as well remove the SessionMiddleware line from MIDDLEWARE and 'django.contrib.sessions' from your INSTALLED_APPS. 



    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
        
        

print(request.session.keys())


 request.session['has_commented'] = True
 
 
 
# Cookie

    response = render(request,'shop/home.html', {'shop': shop, 'form': form, 'pizzas': pizzas})
    response.set_cookie('cookie_name', 'cookie_value')
    return response
    
    
if 'cookie_name' in request.COOKIES:
    value = request.COOKIES['cookie_name']
