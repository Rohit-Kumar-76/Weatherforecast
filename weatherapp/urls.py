# weatherapp/urls.py

from django.contrib import admin
from django.urls import path
from forecast import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.weather, name='weather'),  # Home page
]
