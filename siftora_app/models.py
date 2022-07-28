from django.db import models


class Product(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    shade = models.CharField(max_length=50, blank=True)
    finish = models.CharField(max_length=50, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    open_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    use_count = models.PositiveIntegerField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    will_repurchase = models.BooleanField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} by {self.brand}'


class Bin(models.Model):
    title = models.CharField(max_length=50)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.title} ({self.product_count})'
