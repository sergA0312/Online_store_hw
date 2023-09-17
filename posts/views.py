from django.shortcuts import render
# Create your views here.
from posts.models import OnlineStore


def main_view(request):
    return render(request, template_name='layouts/index.html')


def products_view(request):
    product = OnlineStore.objects.all()
    context_data = {
        'products': product
    }
    return render(request, 'products/products.html', context=context_data)