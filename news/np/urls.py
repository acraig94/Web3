from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles_nz$', views.nz, name='nz'),
    url(r'^articles_international$', views.international, name='international'),
    url(r'^articles_tech$', views.tech, name='tech'),
    url(r'^articles_sport$', views.sport, name='sport'),
    url(r'^article_(?P<pk>\d+)$', views.details, name='article'),
    url(r'^article/new/$', views.article_new, name='article_new'),
]