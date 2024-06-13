from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # My Urls
    path('', views.home_page_view, name='home-page-view')
]
