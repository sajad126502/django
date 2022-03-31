from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from articles.models import Article
from django.contrib.auth.decorators import login_required
import random
@login_required
def index(req):
    article_list_querySet=Article.objects.all()
    str=render_to_string("index.html",{"list":article_list_querySet})
    return HttpResponse(str)
