from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from posts import views as posts_views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('Onlinestore.urls')),
    path('admin/', admin.site.urls),
    path("", posts_views.main_view),
    path("products/", posts_views.products_view),
]



# urls.py

from django.urls import path
from posts import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
]

#Users_aut
from django.urls import path
from django.urls import path
from usersaut.views import register_view, login_view, logout_view

urlpatterns = [
    path('registration/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Добавьте другие URL по необходимости
]


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_product/', views.create_product, name='create_product'),
    path('create_review/<int:product_id>/', views.create_review, name='create_review'),



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
