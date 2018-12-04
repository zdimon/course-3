# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from main.parser import Parser

class Command(BaseCommand):

    def handle(self, *args, **options):
        p = Parser()
        p.updateDataFromSite()
        print 'updated succesfully'