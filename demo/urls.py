from django.contrib import admin
from django.urls import path
from . import views
from .views import IndexView,PageView
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('<int:pk>/', PageView.as_view(),name="home"),
    path('create/', views.create,name="create"),
    path('',IndexView.as_view(),name="homedupe"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
