# Authentication through social networks.

https://python-social-auth-docs.readthedocs.io/en/latest/configuration/django.html

## Install plugin

    pip install social-auth-app-django
    
    
    
### Google

https://console.developers.google.com


##You need to add the Google+ API to the list of enabled APIs on the Google Developer Console!!!


    
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '962025118316-j84jb846ci2iguoeo6146as4f8pcp348.apps.googleusercontent.com'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'YSrulr78oGE4s7xiHWXDDdOD'


## Settings

### Social

    AUTHENTICATION_BACKENDS = (
        'social_core.backends.open_id.OpenIdAuth',
        'social_core.backends.google.GoogleOpenId',
        'social_core.backends.google.GoogleOAuth2',
        'social_core.backends.google.GoogleOAuth',
        'social_core.backends.twitter.TwitterOAuth',
        'social_core.backends.yahoo.YahooOpenId',
        'django.contrib.auth.backends.ModelBackend',
    )

    INSTALLED_APPS += ['social_django']


    SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

## Routings

    url('', include('social_django.urls', namespace='social'))
    
    
Link

        
    <a href="{% url "social:begin" "google-oauth2" %}">Google+</a>

## NGINX
    
    location / {
                proxy_pass http://127.0.0.1:8080;
                proxy_set_header Host "quizer.com.ua";
        }
