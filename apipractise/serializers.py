from rest_framework import serializers

from apipractise.models import Customer


class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','email','phone']



class Customerproductsserializer(serializers.ModelSerializer):
    customer_products = serializers.StringRelatedField(read_only=True,many=True)
    class Meta:
        model = Customer
        fields = ['name','customer_products']