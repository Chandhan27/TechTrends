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