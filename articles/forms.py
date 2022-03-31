from cProfile import label
from dataclasses import fields
from pyexpat import model
from turtle import title
from unittest.util import _MAX_LENGTH
from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=["title","content"]
    def clean(self):
        data=self.cleaned_data
        title=data.get("title")
        qs=Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title","title is already taken")
        return data

# class ArticleFormOld(forms.Form):
#     title=forms.CharField()
#     content=forms.CharField()
   
#     def clean(self):
#         cleaned_data=self.cleaned_data #dictionary
#         if cleaned_data.get('title')=="sajad":
#             self.add_error("title","this title is taken already")
#             # raise forms.ValidationError("sajad is not allowed")
#         print(cleaned_data)
#         return cleaned_data   
        