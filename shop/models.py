from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_at']


class PurchaseHistory(models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    items_purchased = models.TextField()

    class Meta:
        ordering = ['-purchase_date']

    def __str__(self):
        return f"Purchase on {self.purchase_date.strftime('%Y-%m-%d %H:%M')} - ${self.total_amount}"
