from django.db import models
from .models import *

# Create your models here.
class Product(models.Model):
    AVAILABLE = 'available'
    OUT_OF_STOCK = 'out_of_stock'

    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),  
        (OUT_OF_STOCK, 'Out of Stock'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=AVAILABLE  
    )

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.stock <= 0:
            self.status = self.OUT_OF_STOCK
        else:
            self.status = self.AVAILABLE
        super(Product, self).save(*args, **kwargs)  
        
        


# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)  # The ordered product
#     quantity = models.PositiveIntegerField()  # Quantity ordered
#     price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price before discount
#     discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Discount percentage
#     final_price = models.DecimalField(max_digits=10, decimal_places=2)  # Final price after discount

#     def save(self, *args, **kwargs):
#         """Override save method to automatically calculate the final price."""
#         self.price = self.product.price * self.quantity
#         discount_amount = self.price * (self.discount / 100)
#         self.final_price = self.price - discount_amount
#         super().save(*args, **kwargs)
        
#         if self.quantity <= self.product.stock:  # Ensure there's enough stock
#             self.product.stock -= self.quantity
#             self.product.save()  # Save the product to update stock
        
#         super(Order, self).save(*args, **kwargs)

    
#     def __str__(self):
#         return f"Order of {self.quantity} {self.product.name}(s)"

from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  # The user who placed the order
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # The ordered product
    quantity = models.PositiveIntegerField()  # Quantity ordered
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price before discount
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Discount percentage
    final_price = models.DecimalField(max_digits=10, decimal_places=2)  # Final price after discount

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        discount_amount = self.price * (self.discount / 100)
        self.final_price = self.price - discount_amount
        super().save(*args, **kwargs)
        
        if self.quantity <= self.product.stock:
            self.product.stock -= self.quantity
            self.product.save()
        
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order of {self.quantity} {self.product.name}(s)"
