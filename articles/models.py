from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(default="welcome to site")
    

########################################################returning html page from templates folder"
#in setting  'DIRS': ['/Users/sajadbashir/Dev/newDjangoProject/templates']

# from django.http import HttpResponse
# from django.template.loader import render_to_string

# def index(req):
#     str=render_to_string("index.html")
#     return HttpResponse(str)
###########with sending data
#in template html file
#<h1>THIS DATA IS COMING FROM TEMPALTES{{ title }}</h1>

# def index(req):
#     random_id=random.randint(1,4)
#     article_obj=Article.objects.get(id=random_id)
#     str=render_to_string("index.html",{"title":article_obj.title})
#     return HttpResponse(str)




####################template inhirtance ###################
##index.html file
#  ##########base.html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     {% block content %}
#     {% endblock content %}
# </body>
# </html>







#############################LISTING DATA IN VIEWS

#index.html--
# <body>
#         <ul>
#             {% for i in list %}
#             <li>{{ i }}</li>
#             {% endfor %}
#         </ul>
# </body>

#views.py--
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.template.loader import render_to_string
# from articles.models import Article
# import random
# def index(req):
#     data=[1,2,3,4,5]
#     str=render_to_string("index.html",{"list":data})
#     return HttpResponse(str)
#---------------output
# .1
# .2
# .3
# .4
# .5
########another example listing database data in views
#index.html
# <body>
#         <ul>
#             {% for i in list %}
#             <li>{{ i.title }}</li>
#             {% endfor %}
#         </ul>  
# </body>

#views.py
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.template.loader import render_to_string
# from articles.models import Article
# import random
# def index(req):
#     article_list_querySet=Article.objects.all()
#     str=render_to_string("index.html",{"list":article_list_querySet})
#     return HttpResponse(str)


# -----------output
# .this is my first title
# .this is my second title
# .this is my 3rd title
# .Another title






##########################################################working with models

# >>> from dataclasses import dataclass
# >>> @dataclass
# ... class BlogPost:
# ...      content:str
# ...      title:str
# ...      
# >>> obj=BlogPost(title="hello world",content="this is cool")
# >>> obj.title
# 'hello world'
# >>> obj.content
# 'this is cool'
# >>> 



# >>> from articles.models import Article
# >>> obj=Article()
# >>> obj.title
# ''
# >>> obj=Article(title="this is my first title",content="hello world")
# >>> obj.save()
# >>> obj=Article(title="this is my second  title",content="hello again")
# >>> obj.save()
# >>> obj.title
# 'this is my second  title'
# >>> obj=Article.objects.create(title="this is my 3rd  title",content="hello again and again")
# >>> obj.title
# 'this is my 3rd  title'
# >>> Article.objects.all()
# <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
# >>> obj=Article()
# >>> obj.title="Another title"
# >>> obj.content="some more content "
# >>> obj.save()
# >>> Article.objects.all()
# <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>]>
# >>> 

#####Reading#########
# >>> obj=Article.objects.get(id=1)
# >>> obj
# <Article: Article object (1)>
# >>> obj.title
# 'this is my first title'
################################################ADMIN PANEL (register Article model and some more functionality to the admin panel)####
# from django.contrib import admin
# from .models import Article
# # Register your models here.
# class ArticleAdmin(admin.ModelAdmin):
#     list_display=['id','title']
#     search_fields=['title','content']
# admin.site.register(Article,ArticleAdmin)