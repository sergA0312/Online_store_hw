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




from django.shortcuts import render
from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category.html', {'categories': categories})



# views.py

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, ' products/product.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, ' products/product_detali.html', {'product': product})
