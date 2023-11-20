from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apipractise.models import Customer, Product
from apipractise.serializers import Customerserializer, Customerproductsserializer, Productserializer


# Create your views here.
@api_view(['GET'])
def get_all_customers(request):
    customers = Customer.objects.all()
    serializer = Customerserializer(instance=customers,many=True)
    if request.method == 'GET':
        return Response({"All customers":serializer.data})
    else:
        return Response({"Error":"Invalid request method"})


@api_view(['GET'])
def get_one_customer(request,id):
    try:
        customer = Customer.objects.get(pk=id)
        serializer = Customerserializer(instance=customer)
        return Response({"Data":serializer.data})
    except:
        return Response({"Error":"Customer with given id not found"})


@api_view(['PUT','PATCH'])
def update_customer(request,id):
    try:
        customer = Customer.objects.get(pk=id)
        serializer = Customerserializer(instance=customer,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Updated successfully":serializer.data})
    except:
        return Response({"Error":"Couldnt find customer with given id"})

@api_view(['DELETE'])
def delete_customer(request,id):
    try:
        customer = Customer.objects.get(pk=id)
        customer.delete()
        return Response({"Message":f"Customer with id {id} has been deleted successfully"})
    except:
        return Response({"Error":"Customer with given id not found"})

@api_view(['POST'])
def create_customer(request):
    if request.method == 'POST':
        serializer = Customerserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Created customer":serializer.data},status=201)
    else:
        return Response({"Error":"Invalid request method for the endpoint "})



@api_view(['GET'])
def get_customer_products(request,id):
    try:
        customer = Customer.objects.get(pk=id)
        serializer = Customerproductsserializer(instance=customer)
        return Response({"Customer":serializer.data})
    except:
        return Response({"Error" :"Customer with given id not found"})

@api_view(['GET'])
def get_product_details(request,product_id):
    try:
        product = Product.objects.get(pk=product_id)
        serializer = Productserializer(instance=product)
        return Response({"Product details":serializer.data})
    except:
        return Response({"Error":"Product with given id not found"})