from django.shortcuts import render
from .models import Poem, Category
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    poems = Poem.objects.all()
    paginator = Paginator(poems, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    # ctx = {'poems': poems}
    ctx = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'main/index.html', ctx)


def poem(request, pk):
    poem = Poem.objects.get(pk=pk)
    return render(request, 'main/poem.html', {'poem': poem})


def tags_list(request):
    tags = Category.objects.all()
    return render(request, 'main/tags_list.html', context={'tags': tags})
