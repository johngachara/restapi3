from django.contrib import admin

from apipractise.models import Customer, Category, Product, Warranty

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Warranty)
