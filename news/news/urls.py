"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('np.urls')),
    #url(r'^articles_nz', include('np.urls')),
    #url(r'^articles_international', include('np.urls')),
    #url(r'^articles_tech', include('np.urls')),
    #url(r'^articles_sport', include('np.urls')),
]
