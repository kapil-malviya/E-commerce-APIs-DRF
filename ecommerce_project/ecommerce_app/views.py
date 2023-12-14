# Import necessary modules and classes from Django Rest Framework

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Product as ProductModel, Order, OrderItem
from .serializers import CustomerSerializer, ProductSerializer, OrderItemSerializer, OrderSerializer
from django.shortcuts import get_object_or_404



# Define class for listing and creating customers
class CustomerList(APIView):
    def get(self, request):
        # Retrieve all customers from the database
        customers = Customer.objects.all()
        # Serialize the customer data using CustomerSerializer
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Deserialize incoming data and validate it using CustomerSerializer
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            # Save the valid data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define a class for retrieving, updating, and deleting a specific customer
class CustomerDetail(APIView):
    def get_object(self, pk):
        # Get customer instance by primary key or return 404 if not found
        return get_object_or_404(Customer, pk=pk)

    def get(self, request, pk):
        # Retrieve a specific customer and serialize the data
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        # Retrieve a specific customer, deserialize and validate incoming data
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            # Save the updated data to the database
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Retrieve a specific customer and delete it
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Define class for listing and creating products
class Product(APIView):
    def get(self, request):
        # Retrieve all products from the database
        products = ProductModel.objects.all()
        # Serialize the product data using ProductSerializer
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Deserialize incoming data and validate it using ProductSerializer
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            # Save the valid data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define a class for listing and creating orders
class OrderList(APIView):
    def get(self, request):
        # Retrieve all orders from the database
        orders = Order.objects.all()
        # Serialize the order data using OrderSerializer
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Deserialize incoming data and validate it using OrderSerializer
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            # Save the valid data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define a class for retrieving and updating a specific order
class OrderDetail(APIView):
    def get_object(self, pk):
        # Get the order instance by primary key or return 404 if not found
        return Order.objects.get(pk=pk)

    def put(self, request, pk):
        # Retrieve a specific order, deserialize and validate incoming data
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            # Save the updated data to the database
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define class for retrieving orders by specified products
class OrderByProduct(APIView):
    def get(self, request):
        # Get product names from query parameters
        product_names = request.query_params.getlist('products', [])
        # Filter orders by products and serialize the data
        orders = Order.objects.filter(order_items__product__name__in=product_names).distinct()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


# Define class for retrieving orders by specified customer
class OrderByCustomer(APIView):
    def get(self, request):
        # Get customer name from query parameters
        customer_name = request.query_params.get('customer', '')
        # Filter orders by customer and serialize the data
        orders = Order.objects.filter(customer__name=customer_name)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
