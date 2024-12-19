from django.shortcuts import render
from .models import ProductModel, CategoryModel, ImageModel, DocumentModel
# Create your views here.

def product_list(request):
    products = ProductModel.objects.all()
    context = {"products":products}
    return render(request, 'product/pl.html', context=context)


def product_detail(request, slug):
    product = ProductModel.objects.get(slug=slug)
    context = {"product":product}
    return render(request, 'product/product_detail.html', context=context)