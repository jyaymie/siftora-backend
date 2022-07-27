from django.db import models


class Bin(models.Model):
    title = models.CharField(max_length=50)
    product_amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title} ({self.product_amount})'


class Product(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    shade = models.CharField(max_length=50)
    texture = models.CharField(max_length=50)
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    open_date = models.DateField()
    expiry_date = models.DateField()
    uses = models.PositiveIntegerField()
    finish_date = models.DateField()
    will_repurchase = models.BooleanField()
    notes = models.TextField()
