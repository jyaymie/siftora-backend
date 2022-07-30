from django.db import models


class Bin(models.Model):
    title = models.CharField(max_length=100)
    products = models.ManyToManyField(
        'Product', related_name='bins', blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Product(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    shade = models.CharField(max_length=100, blank=True)
    finish = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    open_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    use_count = models.PositiveIntegerField(default=0)
    finish_date = models.DateField(null=True, blank=True)
    will_repurchase = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name} by {self.brand}'
