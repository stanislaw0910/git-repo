from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test),
]
'''
urlpatterns = [
    path (r'^$', views.index),
    path(r'^login/', views.index),
    path(r'^signup/', views.index),
    path(r'^question/\d+/', views.index),
    path(r'^ask/', views.index),
    path(r'^popular/', views.index),
    path(r'^new/', views.index),
]'''