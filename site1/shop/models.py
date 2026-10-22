from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField("Tên món", max_length=100)
    description = models.TextField("Mô tả", blank=True)
    price = models.DecimalField("Giá (đ)", max_digits=10, decimal_places=0)
    image_url = models.URLField("Link ảnh", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = [
        ('placed', 'Đã đặt'),
        ('cancelled', 'Đã hủy'),
        ('refunded', 'Đã hoàn'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS, default='placed')
    created_at = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.food.price * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.food.name} x{self.quantity}"
