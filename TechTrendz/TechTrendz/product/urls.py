from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path("products/", product_list, name="product_list"),
    path("<str:slug>/", product_detail, name="detail"),
]