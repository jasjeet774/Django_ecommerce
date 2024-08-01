from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    image=models.ImageField(upload_to="product")

    def __str__(self):
        return  self.name
    
class Order(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return f'order {self.id}'
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name="items",on_delete=models.CASCADE)    
    product=models.ForeignKey(Product,related_name="order_items",on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return  f'{self.quantity} of {self.product.name}'