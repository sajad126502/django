
from multiprocessing import context
from tkinter import N
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from .forms import ArticleForm
def detailView(req,id=None):
        context=Article.objects.get(id=id)
        return render(req,"base.html",{"context":context})

def article_search(req):
    query_dict=req.GET
    try:
        query=int(query_dict.get("id"))
    except:
        query=None
        context=None
    if(query is not None):
       context=Article.objects.get(id=query)
    return render(req,"search.html",{"context":context})

def createArticle(req):
    context={"form":ArticleForm()}
    # print(dir(ArticleForm()))
    if req.method=="POST":
        form=ArticleForm(req.POST)
        context['form']=form
        print(form)
        if form.is_valid():
            ############## with model form ##############
            article_obj=form.save()
            #############without model forms###########
            # print(form.cleaned_data)
            # title=form.cleaned_data.get("title")
            # content=form.cleaned_data.get("content")
            #     # query_dict=req.POST
            #     # title=query_dict.get("title")
            #     # content=query_dict.get("content")
            # article_obj=Article.objects.create(title=title,content=content)
            context["object"]=article_obj
            context["created"]=True
    return render(req,"create.html",context)
