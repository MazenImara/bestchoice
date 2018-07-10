from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('switch_lang', views.switch_lang, name='switch_lang'),
    path('manageApk', views.manageApk, name='manageApk'),
]