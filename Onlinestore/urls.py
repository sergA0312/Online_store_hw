from django.contrib import admin
from django.urls import path
from posts import views as posts_views



urlpatterns = {
    path('', posts_views.greetings_views, name='greetings'),
    path('', posts_views.now_date, name='now_date'),
    path('', posts_views.goodby, name='goodby')}









