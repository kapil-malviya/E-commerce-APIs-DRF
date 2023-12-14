# Import necessary module for defining URL patterns
from django.urls import path

# Import views from the same Django app (ecommerce_app)
from .views import CustomerList, CustomerDetail, Product, OrderList, OrderDetail, OrderByProduct, OrderByCustomer
 

# Define URL patterns for different views

urlpatterns = [

    # URL pattern for listing and creating customers
    path('customers/', CustomerList.as_view(), name='customer-list'),

    # URL pattern for retrieving, updating, and deleting a specific customer
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),

    # URL pattern for listing and creating products
    path('products/', Product.as_view(), name='products'),

    # URL pattern for listing and creating orders
    path('orders/', OrderList.as_view(), name='order-list'),

    # URL pattern for retrieving and updating a specific order
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),

    # URL pattern for retrieving orders by specified products
    path('orders/by_product/', OrderByProduct.as_view(), name='order-by-product'),

    # URL pattern for retrieving orders by specified customer
    path('orders/by_customer/', OrderByCustomer.as_view(), name='order-by-customer'),
]
