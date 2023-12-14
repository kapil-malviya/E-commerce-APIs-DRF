from django.db import models

# Customer Model

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


# Product Model

class Product(models.Model):
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


# Order Model

class Order(models.Model):
    order_number = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.CharField(max_length=255)


    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.order_by('-id').first()
            if last_order:
                order_number = int(last_order.order_number[3:]) + 1
            else:
                order_number = 0
            self.order_number = f"ORD{int(order_number) + 1:05d}"
            Order.objects.update_or_create(
                order_number=self.order_number,
                defaults={'order_number': F('order_number')}
            )
        super().save(*args, **kwargs)


    def __str__(self):
        return self.order_number


# OrderItem Model

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product} - {self.quantity} units"
