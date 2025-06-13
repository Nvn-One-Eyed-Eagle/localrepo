from django.contrib import admin
from django.urls import path
from .views import home,detail_news

urlpatterns = [
    path('',home,name = 'home'),
    path("detail/<int:pk>/",detail_news,name="detail_news"),
]
