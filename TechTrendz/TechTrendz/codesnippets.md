[TOC]
## Code Snippets
### Web App
#### base.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="{% static 'favicon/favicon-16x16.png' %}" type="image/x-icon">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>{% block title %}{% endblock title %}</title>
</head>

<body>
    {% include 'snippets/navbar.html' %}

    {% block content %}
    {% endblock content %}

    {% include 'snippets/footer.html' %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</body>

</html>
```
---
### navbar.html
```html
<nav class="navbar navbar-expand-lg navbar-light bg-warning">
  <div class="container-fluid">
    <a class="navbar-brand" href="{% url 'web:home' %}"><img src="./../../media/techtrendz_logo.png" alt="logo"
        width="40" height="40"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-center" id="navbarSupportedContent">
      <!-- <ul class="nav justify-content-end"> -->
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="{% url 'web:home' %}">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="{% url 'web:about' %}">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="{% url 'product:product_list' %}">Projects</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="{% url 'web:contact' %}">Contact</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="admin/" target="_blank">Admin</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```
---
### footer.html
```html
<!-- Footer -->
<footer class="text-center text-lg-start bg-warning">
  <!-- Section: Social media -->
  <!-- Left -->

  <!-- Right -->
  <div>
    <a href="" class="me-4 text-reset">
      <i class="fab fa-facebook-f"></i>
    </a>
    <a href="" class="me-4 text-reset">
      <i class="fab fa-twitter"></i>
    </a>
    <a href="" class="me-4 text-reset">
      <i class="fab fa-google"></i>
    </a>
    <a href="" class="me-4 text-reset">
      <i class="fab fa-instagram"></i>
    </a>
    <a href="" class="me-4 text-reset">
      <i class="fab fa-linkedin"></i>
    </a>
    <a href="" class="me-4 text-reset">
      <i class="fab fa-github"></i>
    </a>
  </div>
  <!-- Right -->
  </section>
  <!-- Section: Social media -->

  <!-- Section: Links  -->
  <section class="">
    <div class="container text-center text-md-start mt-5">
      <!-- Grid row -->
      <div class="row mt-3">
        <!-- Grid column -->
        <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
          <!-- Content -->
          <h6 class="text-uppercase fw-bold mb-4">
            <i class="fas fa-gem me-3"></i>TECHTRENDZ
          </h6>
          <p>
            TechTrendz is an innovative <br>
            E-commerce platform that brings the latest tech products and trends.
          </p>
        </div>
        <!-- Grid column -->

        <!-- Grid column -->
        <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">
            Useful links
          </h6>
          <p>
            <a href="{% url 'web:home' %}" class="text-reset">Home</a>
          </p>
          <p>
            <a href="{% url 'web:about' %}" class="text-reset">About</a>
          </p>
          <p>
            <a href="{% url 'product:product_list' %}" class="text-reset">Projects</a>
          </p>
          <p>
            <a href="{% url 'web:contact' %}" class="text-reset">Contact</a>
          </p>
          <p>
            <a href="" class="text-reset">Sitemaps</a>
          </p>
        </div>
        <!-- Grid column -->

        <!-- Grid column -->
        <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">
            Products
          </h6>
          <p>
            <a href="#!" class="text-reset">Temp</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Temp</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Temp</a>
          </p>
          <p>
            <a href="#!" class="text-reset">Temp</a>
          </p>
        </div>
        <!-- Grid column -->


        <!-- Grid column -->
        <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">Contact</h6>
          <p>
            <i class="fas fa-envelope me-3"></i>
            <a href="mailto:techtrendzdsu@gmail.com">techtrendzdsu@gmail.com</a>
          </p>
        </div>
        <!-- Grid column -->
      </div>
      <!-- Grid row -->
    </div>
  </section>
  <!-- Section: Links  -->

  <!-- Copyright -->
  <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
    © Copyright
    <a class="text-reset fw-bold" href="{% url 'web:home' %}">TechTrendz</a>
    2024
  </div>
  <!-- Copyright -->
</footer>
<!-- Footer -->
 ```

 ---

## Product App
### index.html

```html
{% extends 'base.html' %}

{% block title %}
TechhTrendz | Home
{% endblock title %}

{% block content %}

<div id="carouselExampleCaptions" class="carousel slide">
    <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active"
            aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1"
            aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2"
            aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img src="./../../../media/img1.jpg" alt="..." width="1300" height="500">
            <div class="carousel-caption d-none d-md-block">
            </div>
        </div>
        <div class="carousel-item">
            <img src="./../../../media/img2.webp" alt="..." width="1300" height="500">
            <div class="carousel-caption d-none d-md-block">
            </div>
        </div>
        <div class="carousel-item">
            <img src="./../../../media/img3.jpg" alt="..." width="1300" height="500">
            <div class="carousel-caption d-none d-md-block">
            </div>
        </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
</div>
<br><br><br>

<br>
<hr>
<br>

<!-- project list start -->
<div class="container mt-3">
    <h2 class="text-center mb-4">Our Projects</h2>
    <div class="d-flex justify-content-center">
        <div class="row">

            <div class="col-md-3 mb-3">
                <div class="card h-100">
                    <img src="../../../static/image/project/python_techtrendz.png" class="card-img-top" width="18rem"
                        alt="...">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">Python & Raspberry pi</h5>
                    </div>
                </div>
            </div>

            <div class="col-md-3 mb-3">
                <div class="card h-100">
                    <img src="../../../static/image/project/iot_techtrendz.png" class="card-img-top" width="18rem"
                        alt="...">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">Internet of Things</h5>
                    </div>
                </div>
            </div>

            <div class="col-md-3 mb-3">
                <div class="card h-100">
                    <img src="../../../static/image/project/webapplication_techtrendz.png" class="card-img-top"
                        width="18rem" alt="...">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">Cloud Applications</h5>
                    </div>
                </div>
            </div>

        </div>
    </div>
</div>
<!-- project list start End-->


<br><br>
<br>
<hr>
<br><br>


<div class="page-brakes">
    <div class="m-2 px-2 text-center">
        <h2>Are you confused! How to choose your Project?</h2>
        <br>
        <h3 class="">Book a free appointment with our technical team today.</h3>
        <br>
        <a href="mailto:techtrendzdsu@gmail.com" class="btn bg-warning">Send Message</a>
    </div>
</div>


<br><br>
<hr>
<br><br>

{% endblock content %}
```

---

### about.html
```html

{% extends 'base.html' %}
{% load static %}

{% block title %}
TechTrendz | About
{% endblock title %}

{% block content %}

<!-- Parallax Section -->
<div class="position-relative text-center text-white bg-dark" style="height: 300px;">
    <img class="img-fluid w-100 h-100" src="{% static 'image/project/techtrendz_logo.png' %}" alt="TechTrendz Logo"
        style="opacity: 0.5; object-fit: cover;">
    <div class="position-absolute top-50 start-50 translate-middle text-center">
        <h1 class="display-4 fw-bold">Unleashing the Power of TechTrendz</h1>
    </div>
</div>


<div class="container my-5">
    <!-- Introduction Section -->
    <div class="text-center mb-5">
        <h1 class="display-4">Welcome to TechTrendz</h1><br><br>
        <p class="lead">Your one-stop destination for all things tech. Discover the latest gadgets, electronics, and
            smart devices.</p><br>
        <img src="{% static 'image/project/techtrendz_logo.png' %}" alt="TechTrendz Logo" class="img-fluid mb-3"
            style="max-height: 200px;">
    </div>


    <!-- Our Mission Section -->
    <div class="mb-5">
        <h2 class="text-center text-warning">Our Mission</h2>
        <p class="text-justify">Our mission is to revolutionize the way you experience and purchase technology. We
            strive to make high-quality tech products accessible to everyone, ensuring you stay ahead of the curve in
            this rapidly evolving digital age.</p>
    </div>

    <!-- Our Story Section -->
    <div class="mb-5">
        <h2 class="text-center text-warning">Our Story</h2>
        <p class="text-justify">TechTrendz was founded by a team of tech enthusiasts and professionals who
            recognized the need for a reliable platform that offers the newest and most innovative tech products. Since
            our inception, we've grown rapidly, thanks to our commitment to quality, customer satisfaction, and staying
            ahead of the trends.</p>
    </div>

    <!-- What We Offer Section -->
    <div class="mb-5">
        <h2 class="text-center text-warning">What We Offer</h2>
        <ul>
            <li><strong>Diverse Product Range:</strong> From electronics circuits and gadgets to smart home devices and
                we offer a vast selection of products to cater to all your tech needs.</li>
            <li><strong>Expert Reviews and Blogs:</strong> Stay informed with our in-depth product reviews, tech news
                updates, and informative blog articles.</li>
            <li><strong>Community Engagement:</strong> Join our interactive forums to connect with like-minded tech
                enthusiasts, share your experiences, and get advice.</li>
        </ul>
    </div>

    <!-- Our Values Section -->
    <div class="mb-5">
        <h2 class="text-center text-warning">Our Values</h2>
        <ul>
            <li><strong>Innovation:</strong> We believe in the power of innovation and constantly seek out the newest
                tech products to offer our customers.</li>
            <li><strong>Quality:</strong> Quality is at the core of everything we do. We carefully curate our product
                selection to ensure we only offer the best.</li>
            <li><strong>Customer Satisfaction:</strong> Our customers are our top priority. We strive to provide
                excellent customer service and support to ensure a seamless shopping experience.</li>
        </ul>
    </div>

    <!-- Our Journey So Far Section -->
    <div class="mb-5">
        <h2 class="text-center text-warning">Our Journey So Far</h2>
        <p class="text-justify">Since our launch, we've achieved several milestones that we're incredibly proud of.
            We've expanded our product range, grown our customer base, and built a community of tech enthusiasts who
            share our passion for innovation.</p>
    </div>

    <!-- Looking Ahead Section -->
    <div class="mb-5">
        <h2 class="text-center text-warning">Looking Ahead</h2>
        <p class="text-justify">The future is bright for TechTrendz. We plan to continue expanding our product
            offerings, improving our platform, and fostering a community of tech lovers who are as excited about the
            future of technology as we are.</p>
    </div>
</div>

<!-- Meet the Team Section -->
<div class="mb-5">
    <h2 class="text-center text-warning">Meet the Team</h2>
    <div class="row text-center">
        <div class="col-md-3 mb-4">
            <img src="{% static 'image/img1.png' %}" class="img-fluid" width="200" height="150" alt="Abhishek C">
            <h5>Abhishek C</h5>
            <h6>(ENG23CS1001)</h6>
            <p>Founder and CEO</p>
        </div>
        <div class="col-md-3 mb-4">
            <img src="{% static 'image/img2.png' %}" class="img-fluid" width="200" height="150" alt="Akshata Athani">
            <h5>Akshata M Athani</h5>
            <h6>(ENG23CS1022)</h6>
            <p>Chief Technology Officer</p>
        </div>
        <div class="col-md-3 mb-4">
            <img src="{% static 'image/img3.png' %}" class="img-fluid" width="200" height="150" alt="S Chandhan">
            <h5>S Chandhan</h5>
            <h6>(ENG23CS1017)</h6>
            <p>Head of Product Development</p>
        </div>
        <div class="col-md-3 mb-4">
            <img src="{% static 'image/img4.png' %}" class="img-fluid" width="200" height="150" alt="Saraswathi S">
            <h5>Saraswathi S</h5>
            <h6>(ENG22CS1052)</h6>
            <p>Marketing Director</p>
        </div>
    </div>
</div>


<!-- Guided By Section -->
<div class="container my-5">
    <h2 class="text-center text-warning" style="font-family: 'Akronim';">Guided By:</h2>
    <div class="row text-center">
        <div class="col">
            <img src="{% static 'image/img5.png' %}" class="img-fluid" width="250" height="150" alt="Nandini K">

            <h5 style="font-family: monospace; margin-top: 0; margin-bottom: 0;">Ms Nandini K</h5>
            <p style="margin-top: 0; margin-bottom: 0;">Guide</p>
            <p style="margin-top: 0; margin-bottom: 0;">Assistant Professor, Dept OF CSE</p>
            <p style="margin-top: 0; margin-bottom: 0;">Dayananda Sagar University</p>
        </div>
    </div>
</div>

<br><br>
{% endblock content %}
```

---

## Projects
> In Projects there are two pages list.html and detail.html
### project_list.html
```html
{% extends 'base.html' %}

{% block title %}
TechTrendz | Products
{% endblock title %}

{% block content %}
<div class="container mt-3">
    <h2 class="text-center mb-4">Our Projects</h2>
    <div class="row">
        {% for product in products %}
        <div class="col-md-3 mb-3">
            <div class="card h-100">
                {% for p_image in product.images.all %}
                <img src="{{p_image.image.url}}" class="card-img-top" width="40" height="100" alt="{{p_image.name}}">
                {% endfor %}
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">{{product.name}}</h5>
                    <p class="card-text">{{product.details|truncatewords:15 }}</p>
                    <a href="{% url 'product:detail' product.slug %}" class="btn btn-primary mt-auto bg-warning">Read
                        More</a>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock content %}
```

### product_detail.html
```html
{% extends 'base.html' %}

{% block title %}
{{product.name}} | TechTrendz
{% endblock title %}

{% block content %}
<br><br>
<div class="container mt-4">
    <div class="row">
        <div class="col-md-6">
            <!-- Product Images -->
            <div id="productImagesCarousel" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-inner">
                    {% for p_image in product.images.all %}
                    <div class="carousel-item {% if forloop.first %}active{% endif %}">
                        <img src="{{p_image.image.url}}" class="d-block w-100" alt="{{p_image.name}}"
                            style="height: 500px; object-fit: cover;">
                    </div>
                    {% endfor %}
                </div>
                <button class="carousel-control-prev" type="button" data-bs-target="#productImagesCarousel"
                    data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#productImagesCarousel"
                    data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </div>
        <div class="col-md-6">
            <!-- Product Details -->
            <h2 class="text-center">{{product.name}}</h2>
            <p>{{product.details}}</p>

            <!-- Product Documents -->
            {% if product.documentmodel_set.all %}
            <br><br>
            <a href="https://forms.gle/kBFs3SsYX4hfkqsU9" class="btn bg-warning">For More Info Contact US</a>

            <h5 class="mt-4">Documents</h5>
            <ul class="list-group">
                {% for p_docs in product.documentmodel_set.all %}
                <li class="list-group-item">
                    <a href="{{p_docs.doc.url}}">{{p_docs.name}}</a>
                </li>
                <!-- <br><br>
                    <a href="https://forms.gle/kBFs3SsYX4hfkqsU9" class="btn bg-warning">For More Info Contact US</a> -->

                {% endfor %}
            </ul>
            {% endif %}
        </div>
    </div>
</div>
<br><br><br>
{% endblock content %}
```

---

contact.html
```html
{% extends 'base.html' %}
{% load static %}

{% block title %}
TechTrendz | Contact
{% endblock title %}

{% block content %}
<div class="container my-5">
    <h1 class="text-center mb-4 text-warning">Get in Touch with TechTrendz</h1>
    <br>
    <!-- Contact Information -->
    <div class="row mb-5">
        <div class="col-md-6">
            <h2>Contact Information</h2>
            <p>We're here to help! Whether you have a question about our products, need support, or just want to share
                your feedback, feel free to reach out to us through any of the following methods.</p>
        </div>
    </div>
    <div class="col-md-6">
        <h2>Send Us a Message</h2>
        <form>
            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" placeholder="Your Name">
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" placeholder="Your Email">
            </div>
            <div class="mb-3">
                <label for="message" class="form-label">Message</label>
                <textarea class="form-control" id="message" rows="4" placeholder="Your Message"></textarea>
            </div>
            <button type="submit" class="btn btn-primary bg-warning">Send Message</button>
        </form>
    </div>
</div>

<!-- Phone and Email -->
<!-- <div class="row mb-5">
        <div class="col-md-6">
            <h2>Call Us</h2>
            <p><strong>Customer Service:</strong> +1 (123) 456-7890</p>
            <p><strong>Technical Support:</strong> +1 (987) 654-3210</p>
        </div>
        <div class="col-md-6">
            <h2>Email Us</h2>
            <p><strong>General Inquiries:</strong> info@techtrendz.com</p>
            <p><strong>Support:</strong> support@techtrendz.com</p>
        </div>
    </div> -->

<!-- Address -->
<!-- <div class="row mb-5">
        <div class="col-md-12">
            <h2>Visit Us</h2>
            <p>TechTrendz Headquarters</p>
            <p>123 Tech Lane</p>
            <p>Innovate City, TechState, 12345</p>
        </div>
    </div> -->

<!-- Social Media -->
<!-- <div class="row mb-5">
        <div class="col-md-12">
            <h2>Connect with Us on Social Media</h2>
            <p>Follow us on our social media channels to stay updated with the latest news, product launches, and more.
            </p>
            <p>
                <a href="https://facebook.com/techtrendz" class="me-2"><i class="fab fa-facebook"></i> Facebook</a>
                <a href="https://twitter.com/techtrendz" class="me-2"><i class="fab fa-twitter"></i> Twitter</a>
                <a href="https://instagram.com/techtrendz" class="me-2"><i class="fab fa-instagram"></i> Instagram</a>
                <a href="https://linkedin.com/company/techtrendz"><i class="fab fa-linkedin"></i> LinkedIn</a>
            </p>
        </div>
    </div> -->

<!-- FAQs -->
<!-- <div class="row">
        <div class="col-md-12">
            <h2>Frequently Asked Questions</h2>
            <p>Before reaching out, you might want to check our <a href="#">FAQs page</a> where we have answered some of
                the most common questions about our products and services.</p>
        </div>
    </div> -->
</div>
{% endblock content %}
```

---

### Web App viewys.py
```py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    template_name = 'web/index.html'
    extra_content = {}

class AboutPage(TemplateView):
    template_name = 'web/about.html'
    extra_content = {}

class AboutPage2(TemplateView):
    template_name = 'web/about2.html'
    extra_content = {}

class ContactPage(TemplateView):
    template_name = 'web/contact.html'
    extra_content = {}

def robot_page(request):
    return render(request, 'web/robot.txt', content_type="text/plain")
```

### Web App urls.py
```py
from django.urls import path
from .views import HomePage, AboutPage, ContactPage, AboutPage2, robot_page


urlpatterns = [
    path("", HomePage.as_view(), name='home'),
    path("about/", AboutPage.as_view(), name='about'),
    path("about2/", AboutPage2.as_view(), name='about2'),
    path("contact/", ContactPage.as_view(), name='contact'),
    path("robot.txt/", robot_page),
]

```
---

### Product App models.py
```py
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
```

### Model App views.py
```py
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
```

Product App urls.py
```py
from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path("products/", product_list, name="product_list"),
    path("<str:slug>/", product_detail, name="detail"),
]
```

Model App admin.py
```py
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
```

---

