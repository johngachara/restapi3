from rest_framework import serializers

from apipractise.models import Customer, Product


class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','email','phone','id']



class Customerproductsserializer(serializers.ModelSerializer):
    customer_products = serializers.StringRelatedField(read_only=True,many=True)
    class Meta:
        model = Customer
        fields = ['name','customer_products']


class Productserializer(serializers.ModelSerializer):
    warranty_provider = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ['product_name','product_price','warranty_provider']