from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'section', 'author', 'createdDate']

admin.site.register(Article, ArticleAdmin)