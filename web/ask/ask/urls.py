"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    /
/login/
/signup/
/question/<123>/    # вместо <123> - произвольный ID
/ask/
/popular/
/new/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from qa import views



urlpatterns = [
    path('', views.test, name='/'),
    path('login/', views.test, name='login'),
    path('signup/', views.test, name='signup'),
    path('question/<int:id>/', views.test, name='question'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.test, name='popular'),
    path('new/', views.test, name='new'),
]
'''
urlpatterns = [
    url (r'^$', include ('qa.urls') ),
    url (r'^login/', include ('qa.urls') ),
    url (r'^signup/', include ('qa.urls')),
    url (r'^question/\d+/', include ('qa.urls')),
    url (r'^ask/', include ('qa.urls')),
    url (r'^popular/', include ('qa.urls')),
    url (r'^new/', include ('qa.urls') ),
]'''
