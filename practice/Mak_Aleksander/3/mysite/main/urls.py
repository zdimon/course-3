from django.urls import path
from .views import home, poem, tags_list


urlpatterns = [
    path('', home),
    path('<int:pk>/', poem),
    path('tags/', tags_list, name='tags_list_url')
]
