from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Article

def index(request):
    article_list = Article.objects.order_by("-public_date")[:5]
    template = loader.get_template("news/index.html")
    context = {
        "article_list": article_list,
    }
    return HttpResponse(template.render(context, request))

def details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "news/detail.html", {"article": article})
