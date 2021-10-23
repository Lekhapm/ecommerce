"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from ecommerce_app import views
# from .views import Productlist
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stores/',views.Storelist.as_view()),
    url(r'^categories/',views.Categorylist.as_view()),
    url(r'^subcategories/',views.Subcategorylist.as_view()),
    url(r'^products/',views.Productlist.as_view()),
    # url(r'^products/(?P<pk>[0-9]+)/',views.Productlist.as_view()),
    # re_path(r'^products/(?P<id>[0-9]+)/', views.Productlist.as_view()),
    url(r'^products/(?P<id>\w+)$', views.Productlist.as_view(),name='Productlist'),
    url(r'^categories/(?P<id>\w+)$', views.Categorylist.as_view(),name='categorylist'),

    url(r'^store_products/',views.Storeproductlist.as_view()),



]
