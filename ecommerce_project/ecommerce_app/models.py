# Import necessary modules for defining models

from django.db import models
from django.db.models import F

 
# Customer Model
class Customer(models.Model):
	# Fields for the Customer model
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
    	# String representation of the Customer model with all fields
        return f"{self.name} - {self.contact_number} - {self.email}"


# Product Model
class Product(models.Model):
	# Fields for the Product model
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
    	# String representation of the Product model with all fields
        return f"{self.name} - {self.weight} kg"


# Order Model
class Order(models.Model):
	# Fields for the Order model
    order_number = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.CharField(max_length=255)


    def save(self, *args, **kwargs):
    	# Generate unique order_number if not provided
        if not self.order_number:
        	# Retrieve the last order to determine the next order number
            last_order = Order.objects.order_by('-id').first()
            if last_order:
                order_number = int(last_order.order_number[3:]) + 1
            else:
                order_number = 0
            # Format the order_number and assign it to the current instance
            self.order_number = f"ORD{int(order_number) + 1:05d}"
            # Ensure order_number uniqueness using update_or_create
            Order.objects.update_or_create(
                order_number=self.order_number,
                defaults={'order_number': F('order_number')}
            )
        # Call the original save method
        super().save(*args, **kwargs)


    def __str__(self):
    	# String representation of the Order model with all fields
        return f"{self.order_number} - {self.customer} - {self.order_date} - {self.address}"


# OrderItem Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
    	# String representation of the OrderItem model with all fields
        return f"{self.order} - {self.product} - {self.quantity} units"
        
