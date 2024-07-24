from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from datetime import datetime
from django.shortcuts import render, redirect
from blog.models import ArticleModel
from django.utils import timezone
from blog.forms import ArticleForm

# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to my blog!")
    def post(self, request):
        return HttpResponse("[POST] Welcome to my blog!")

class Article(View):
    def get(self, request):
        articles = ArticleModel.objects.all()

        return render(request, "articles.html", {"articles": articles, "form": ArticleForm()})

    def post(self, request):
        form = ArticleForm(request.POST)
        form.instance.created_at = datetime.now(tz=timezone.utc)
        form.save()
        return redirect("/blog/articles")

class ArticleDetails(View):
    def get(selfself, request, id):
        try:
            article = ArticleModel.objects.get(id=id)
            return render(request, "article_details.html", {"article": article})
        except ArticleModel.DoesNotExist:
            return HttpResponseNotFound()
