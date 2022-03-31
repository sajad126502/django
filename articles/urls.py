from django.urls import path
from . import views
urlpatterns = [
    path("",views.article_search),
    path("<int:id>",views.detailView),
    path("create",views.createArticle)
]