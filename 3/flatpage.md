##Flatpage

Install sites and flatpages apps.


    INSTALLED_APPS = [
        ....
        'django.contrib.sites',
        'django.contrib.flatpages',
    ]

###Adding tables

    (course_ve)zdimon@desktop:~/www/course_ve/blog$ ./manage.py migrate

### Add SITE_ID variable

    SITE_ID = 1

### Creating page "/about/"

### Creating template dir

    mkdir templates
    cd templates
    mkdir flatpages
    cd flatpages
    echo 'hello' >> default.html

### Add template path


    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR+'/templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

### Add content block

    <!DOCTYPE html>
    <html>

        <head>
            <title>{{ flatpage.title }}</title>
        </head>

        <body>
            {{ flatpage.content }}
        </body>

    </html>

### Inherit from base.html

    {% extends 'base.html' %}
    
    {% block title %} {{ flatpage.title }} {% endblock %}

    {% block content %} {{ flatpage.content }} {% endblock %}
    
### Create base.html

    <!DOCTYPE html>
    <html>

        <head>
            <title>{% block title %} {% endblock %}</title>
        </head>

        <body>
            {% block content %} {% endblock %}
        </body>

    </html>

### Add links


      <div class="navbar navbar-default navbar-fixed-top" >
          <div class="container">
             <ul class="nav navbar-nav">
                  <li><a href="{% url 'about' %}">{% trans 'About us' %}</a></li>
                  <li><a href="{% url 'help' %}">{% trans 'Help' %}</a></li>
                  <li><a href="{% url 'contact' %}">{% trans 'Contacts' %}</a></li>
            </ul>
         </div>
     </div>

### Add named urls

    from django.contrib.flatpages import views

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^pages/', include('django.contrib.flatpages.urls')),
        url(r'^about-us/$', views.flatpage, {'url': '/about/'}, name='about'),
        url(r'^help/$', views.flatpage, {'url': '/help/'}, name='help'),
        url(r'^contact/$', views.flatpage, {'url': '/contact/'}, name='contact'),
    ]



*A "raw string literal" is a slightly different syntax for a string literal, in which a backslash, \, is taken as meaning "just a backslash" (except when it comes right before a quote that would otherwise terminate the literal) -- no "escape sequences" to represent newlines, tabs, backspaces, form-feeds, and so on. In normal string literals, each backslash must be doubled up to avoid being taken as the start of an escape sequence.*









