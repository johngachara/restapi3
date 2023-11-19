"""
URL configuration for djangoProject14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from apipractise import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.get_all_customers,name='all_customers'),
    path('customer/<int:id>',views.get_one_customer,name='one_customer'),
    path('customer/<int:id>/update',views.update_customer,name='update_customer'),
    path('customer/<int:id>/delete',views.delete_customer,name='delete_customer'),
    path('customer/create',views.create_customer,name='create_customer'),
    path('customer/<int:id>/products',views.get_customer_products,name='customer_products')
]
