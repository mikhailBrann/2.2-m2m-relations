from django.shortcuts import render

from articles.models import Article, ArticleTag


def articles_list(request):
    template = 'articles/news.html'
    context = {}


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    articles_query = Article.objects.all().order_by(ordering)
    context['object_list'] = [{"title": article.title, "text": article.text, "image": article.image, "scopes": ArticleTag.objects.all().filter(article_id=article.id)} for article in articles_query]

    return render(request, template, context)