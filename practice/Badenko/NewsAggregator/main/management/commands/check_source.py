# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from django.core.files.base import ContentFile
from main.models import Article
import requests

class Command(BaseCommand):

    def handle(self, *args, **options):
        a = Article()
        aList = a.getAll()
        for i in aList:
            if i.htmlSource == None:
                r = requests.get(i.url)
                srcData = r.text.encode('utf-8')
                srcFile = ContentFile( srcData ) # srcData is the contents of the local file
                srcFile.open()
                i.htmlSource.save(name='%s.html' %i.title, content=srcFile)
                print 'added source code to article %s' %i.url
                