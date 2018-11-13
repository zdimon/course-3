#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from django.conf import settings
from django.conf.urls import include, url
from django.http import HttpResponse


# путь к файлу роутинга

filename = os.path.splitext(os.path.basename(__file__))[0]


# вьюха
def home(request):
    return HttpResponse('File: %s Debug mode: %s' % (filename, settings.DEBUG))


# роутинг
urlpatterns = [
    url(r'^$', home),
]



if __name__ == "__main__":
    settings.configure(
        DEBUG=True,
        MIDDLEWARE_CLASSES = [],
        ROOT_URLCONF = filename
    )

    from django.core.management import execute_from_command_line
    execute_from_command_line([sys.argv[0], 'runserver', sys.argv[1]])
