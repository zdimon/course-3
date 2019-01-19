from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from main.models import Page

def home(request):
    page = Page.objects.get(pk=1)
    return render(request, 'index.html', {'page': page})
    
from django.conf import settings    
    
def change_lang(request):
    language = request.GET.get(u'language', None)
    _next = request.GET.get('next', None)
    for lang in settings.LANGUAGES:
        prefix = '/%s/' % lang[0]
        if _next.startswith(prefix):
            _next = _next[len(prefix):]
    return HttpResponseRedirect('/%s/%s' % (language,_next))
