###Create 'main' applicalion


    ./manage.py startapp main

### Create view.


    from django.template import RequestContext
    from django.shortcuts import render_to_response

    def home(request):
        context = {'page': about}
        return render_to_response('main/home.html', context, RequestContext(request))


###Create template in templates/main/home.html


    {% extends 'base.html' %}
    
    {% block title %} {{ flatpage.title }} {% endblock %}

    {% block content %} 

        <h2> Home page </h2>

        {{ flatpage.content }} 
    
    {% endblock %}

### Add index url

    from main.views import home

    urlpatterns = [
        url(r'^$', home),
        ...
    ]


### Create model


    class Musician(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        instrument = models.CharField(max_length=100)

    class Album(models.Model):
        artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        release_date = models.DateField()
        num_stars = models.IntegerField()

### Create migration

    ./manage.py makemigrations

### Apply migration

    ./manage.py migrate

### Add model to admin app.


    class MusicianAdmin(admin.ModelAdmin):
        pass

    admin.site.register(Musician, MusicianAdmin)


    class AlbumAdmin(admin.ModelAdmin):
        pass

    admin.site.register(Album, AlbumAdmin)    



    
