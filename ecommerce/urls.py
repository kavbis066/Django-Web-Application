"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from ecommerce import views
from django.conf.urls.static import static
from django.conf import settings
#from .views import home_page, about_page, contact_page, login_page, register_page

# app_name = "ecommerce"

urlpatterns = [
    url(r'^$', views.home_page, name="home"),
    url(r'^about/$', views.about_page),
    #url(r'^contact/$', views.contact_page),
    url(r'^login/$', views.login_page, name="login"),
    url(r'^login_page_view/$', views.login_page_view, name="login_page_view"),
    url(r'^register/$', views.register_page, name="register"),
    url(r'^checkout/$', views.checkout, name="checkout"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
