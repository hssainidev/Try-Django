"""
To render html web pages
"""

from articles.models import Article
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
import random

def article_home_view(request):
    return HttpResponse

def home_view(request, *args, **kwargs):
    """
    Take in a request from Django
    Return HTML as a response
    """
    print(id)
    name = "Harpreet"
    number = random.randint(1,4)
    article_obj = Article.objects.get(id=number)
    article_queryset = Article.objects.all

       
    context = {
        "object": article_obj,
        "object_list": article_queryset,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    tmpl = get_template("home-view.html")
    tmpl_string = tmpl.render(context=context)

    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(tmpl_string)