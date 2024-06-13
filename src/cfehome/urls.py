from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # My Urls
    path('', views.home_view, name='home-view'),
    path('about/', views.about_view, name='home-view'),
]
