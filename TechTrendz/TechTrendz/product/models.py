from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class CategoryModel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            unique_slug = slug
            num = 1
            while CategoryModel.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)


class ProductModel(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=600, unique=True, blank=True)
    model_no = models.CharField(max_length=200)
    bill_detail = models.TextField(verbose_name="Text on Bill")
    hsn_code = models.CharField(max_length=100, verbose_name="HSN / SAC Code")
    tax = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="TAX in %")
    details = models.TextField()
    specafications = models.TextField()
    category = models.ManyToManyField(CategoryModel)

    doc = models.DateTimeField(auto_now_add=True)
    doe = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, verbose_name="Visible")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            unique_slug = slug
            num = 1
            while ProductModel.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

class ImageModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="media/product/images/")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')

    def _str_(self):
        return self.name

class DocumentModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    doc = models.FileField(upload_to="media/product/docs/")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def _str_(self):
        return self.name