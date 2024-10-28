from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *


def main(request):
    posts = Article.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    Authors = Author.objects.all()
    context = {
        "Authors": Authors,
        "page_obj": page_obj,
    }
    return render(request, 'pagination.html', context)
