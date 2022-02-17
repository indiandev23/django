from django.contrib import admin
from django.urls import path
from home import views
admin.site.site_header = "PRINCE Admin"
admin.site.site_title = "Prince Admin Portal"
admin.site.index_title = "Welcome to My First Django Website"


urlpatterns = [
   path("", views.index, name='home'),
   path("about", views.about, name='about'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),



]