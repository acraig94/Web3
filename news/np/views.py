from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

def index(request):
    articles = Article.objects.all().annotate().order_by('-createdDate')[:5] #annotate
    return render(request, 'np/article_list.html', {'articles': articles})

def nz(request):
    articles = Article.objects.filter(section='NZ').order_by('-createdDate')
    return render(request, 'np/article_list.html', {'articles': articles})

def international(request):
    articles = Article.objects.filter(section='INTERNATIONAL').order_by('-createdDate')
    return render(request, 'np/article_list.html', {'articles': articles})

def tech(request):
    articles = Article.objects.filter(section='TECH').order_by('-createdDate')
    return render(request, 'np/article_list.html', {'articles': articles})

def sport(request):
    articles = Article.objects.filter(section='SPORT').order_by('-createdDate')
    return render(request, 'np/article_list.html', {'articles': articles})

def details(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'np/article.html', {'article': article})

@login_required
def article_new(request):
    form = ArticleForm()
    return render(request, 'np/article_edit.html', {'form': form})

