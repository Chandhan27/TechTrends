"""
URL configuration for TechTrendz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.contrib.sitemaps import Sitemap
from product.models import ProductModel

class StaticPageSitemap(Sitemap):
    changefreq = "yearly"
    priority = "0.9"

    def items(self):
        return ["web:home", "web:about", "web:contact"]
    
    def location(self, obj):
        return reverse(obj)


class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return ProductModel.objects.all()
    
    def lastmod(self, obj):
        return obj.doe

sitemaps = {
    "static": StaticPageSitemap,
    "products": ProductSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap"
    ),
    path("", include(("web.urls", "web"), namespace="web")),
    path("", include(("product.urls", "product"), namespace="product")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)