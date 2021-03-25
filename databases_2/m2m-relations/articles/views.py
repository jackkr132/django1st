from django.db.models import Prefetch
from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, ArticleSection


# def articles_list(request):
#     template = 'articles/news.html'
#
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     ordering = '-published_at'
#     articles = Article.objects.all()
#     context = {"object_list": articles}
#
#     return render(request, template, context)

def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.order_by('-published_at').prefetch_related(
        Prefetch(
            'article',
            queryset=ArticleSection.objects.select_related(
                'section'
            ).order_by('-main_section'),
        ),
    )
    context = {'object_list': articles}
    return render(request, template, context)
