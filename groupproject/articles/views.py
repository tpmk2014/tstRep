from django.shortcuts import render

from articles.models import Article, Section


def article_view(request, article_section):
  section_id = Section.objects.get(name=article_section).pk
  article = Article.objects.filter(section=section_id)
  context = {"article": article}
  print(article)
  template = "articles/articles.html"
  return render(request, template, context)
