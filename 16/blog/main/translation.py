from modeltranslation.translator import translator, TranslationOptions
from main.models import Page

class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

translator.register(Page, PageTranslationOptions)
