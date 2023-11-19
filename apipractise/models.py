from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=17,unique=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=20)
    def __str__(self):
        return self.category



class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product_category')
    product_price = models.DecimalField(decimal_places=2,max_digits=7)
    products_for_customer = models.ManyToManyField(Customer,related_name='customer_products')
    def __str__(self):
        return self.product_name

class Warranty(models.Model):
    warranty_provider = models.CharField(max_length=20,default='Jumia')
    product_warranty = models.OneToOneField(Product,on_delete=models.CASCADE,related_name='product')
    duration = models.IntegerField()
    def __str__(self):
        return self.warranty_provider

