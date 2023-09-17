from django.contrib import admin
from django.urls import path
from posts import views as posts_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", posts_views .main_view),
    path("products/", posts_views.products_view),
]









