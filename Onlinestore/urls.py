from django.conf import settings
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path
from posts import views as posts_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", posts_views .main_view),
    path("products/", posts_views.products_view),
]


# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





