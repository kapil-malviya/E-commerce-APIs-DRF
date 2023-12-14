from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import validators
from .models import Customer, Product, Order, OrderItem
from django.utils import timezone

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': [validators.UniqueValidator(queryset=Customer.objects.all())]}
        }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': [validators.UniqueValidator(queryset=Product.objects.all())]},
            'weight': {'validators': [MinValueValidator(0), MaxValueValidator(25)]}
        }


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'order_number': {'read_only': True},
            'order_date': {'validators': []},  # Disable default validators for order_date
        }

    def validate(self, data):
        order_date = data.get('order_date')
        if order_date and order_date < timezone.now().date():
            raise serializers.ValidationError("Order Date cannot be in the past.")

        order_items = data.get('order_items', [])
        total_weight = sum(item['product'].weight * item['quantity'] for item in order_items)
        if total_weight > 150:
            raise serializers.ValidationError("Order cumulative weight must be under 150kg.")

        return data

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for order_item_data in order_items_data:
            OrderItem.objects.create(order=order, **order_item_data)
        return order