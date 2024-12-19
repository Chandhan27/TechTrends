from django.contrib import admin
from .models import ProductModel, CategoryModel, ImageModel, DocumentModel

class ImageInline(admin.TabularInline):
    model = ImageModel
    extra = 1
    max_num = 4
    fields = ["image", "name"]

class DocumentInline(admin.TabularInline):
    model = DocumentModel
    extra = 1
    max_num = 4
    fields = ["doc", "name"]


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'model_no', 'hsn_code', 'doc', 'active']
    list_per_page = 2
    inlines = [ImageInline, DocumentInline]


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_filter = ['name']
    list_per_page = 5


# Register your models here.
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ImageModel)
admin.site.register(DocumentModel)