from django.urls import path
from .views import HomePage, AboutPage, ContactPage, AboutPage2, robot_page


urlpatterns = [
    path("", HomePage.as_view(), name='home'),
    path("about/", AboutPage.as_view(), name='about'),
    path("about2/", AboutPage2.as_view(), name='about2'),
    path("contact/", ContactPage.as_view(), name='contact'),
    # path("robot.txt/", robot_page),
]
