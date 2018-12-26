# Static pages

Initialization

    ./manage.py startapp page
    
settings.py

    INSTALLED_APPS += ['page']


## Simple template view

    from django.views.generic import TemplateView


    class InfoView(TemplateView):
        template_name = "page/info.html"

        def get_context_data(self):
            return {'info': 'Hello'}

models.py


    from django.db import models
    from django.urls import reverse
    from django.utils.translation import gettext as _

    class Page(models.Model):
        title = models.CharField(max_length=150, verbose_name=_(u'Заголовок'))
        content = models.TextField(verbose_name=_(u'Содержание'))
        name_slug = models.CharField(max_length=150, verbose_name=_(u'Алиас'))
        meta_title = models.CharField(max_length=150, verbose_name=_(u'Мета-заголовок'))
        meta_keywords = models.CharField(max_length=250, verbose_name=_(u'Мета-словосочитания'))
        meta_description = models.CharField(max_length=250, verbose_name=_(u'Мета-описание'))

        def __unicode__(self):
            return self.title

        def get_absolute_url(self):
            return reverse('show_page', kwargs={'name_slug': self.name_slug})
            
            
Migration

    ./manage.py makemigrations
    ./manage.py migrate
    
    
Load test page command

    from django.core.management.base import BaseCommand
    from django.utils import timezone
    from django.conf import settings
    from page.models import Page
    from django.core.files import File

    class Command(BaseCommand):

        def handle(self, *args, **kwargs):
            print('Создание страницы')
            p = Page()
            p.title = 'Заголовок'
            p.content = 'Содержание'
            p.name_slug = 'Алиас'
            p.meta_title = 'Мета-заголовок'
            p.meta_keywords = 'Мета-словосочитания'
            p.meta_description = 'Мета-описание'
            p.save()
            
            
            
Admin


    from .models import Page


    class PageAdmin(admin.ModelAdmin):
        list_display = ['title','name_slug']

    admin.site.register(Page, PageAdmin)

                
                
## Class based view


    from django.views.generic import TemplateView, DetailView   
    from .models import Page

    class InfoView(DetailView):
        model = Page
        
    
View

    path('info/<int:pk>', InfoView.as_view()),
            
            
            
## Edit page

URL

    path('page/edit/<int:pk>', PageEditView.as_view(), name="edit_page"),            

Link

    <a href="{% url 'edit_page' pk=object.id %}">Edit</a>
    
View

    class PageEditView(UpdateView):
        model = Page  
        fields = ['title', 'content']  
    
Form template

            <form method="POST">
                    {% csrf_token %}
                    {{ form }}
                    <input type="submit" name="Save" value="Save" />
            </form>
            
            
## Wisivig editor

    pip install django-ckeditor


config.py

    INSTALLED_APPS += ['ckeditor']
    CKEDITOR_UPLOAD_PATH = "uploads/"
    
    
url.py

    path('ckeditor', include('ckeditor_uploader.urls')),
    
    
models.py


    from ckeditor.fields import RichTextField

    class Page(models.Model):
        ...
        content = RichTextField(verbose_name=_(u'Содержание'))


            
Additional configs


    CKEDITOR_CONFIGS = {
        'default': {
            'toolbar': 'full',
            'height': 300,
            'width': 800,
        },
    }

            
            
            
