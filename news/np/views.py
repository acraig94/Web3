from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all().order_by('-createdDate')
    return render(request, 'np/index.html', {'articles': articles})

def nz(request):
    articles = Article.objects.filter(section='NZ').order_by('-createdDate')
    return render(request, 'np/index.html', {'articles': articles})

def international(request):
    articles = Article.objects.filter(section='INTERNATIONAL').order_by('-createdDate')
    return render(request, 'np/index.html', {'articles': articles})

def tech(request):
    articles = Article.objects.filter(section='TECH').order_by('-createdDate')
    return render(request, 'np/index.html', {'articles': articles})

def sport(request):
    articles = Article.objects.filter(section='SPORT').order_by('-createdDate')
    return render(request, 'np/index.html', {'articles': articles})

def details(request, article_id):
    articles = Article.objects.get(id=article_id)
    return render(request, 'np/details.html', {'articles': articles})