from django.db import models

class Inventory(models.Model):
    product_name = models.CharField(max_length=200)
    stock_quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name
