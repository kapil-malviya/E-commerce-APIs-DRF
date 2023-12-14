from django.urls import path
from .views import CustomerCreate, CustomerList, CustomerDetail, Product, OrderList, OrderDetail, OrderByProduct, OrderByCustomer

urlpatterns = [
    path('customers/create/', CustomerCreate.as_view(), name='customer-create'),
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    path('products/', Product.as_view(), name='products'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('orders/by_product/', OrderByProduct.as_view(), name='order-by-product'),
    path('orders/by_customer/', OrderByCustomer.as_view(), name='order-by-customer'),
]