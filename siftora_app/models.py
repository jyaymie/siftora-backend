from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_owner(sender, instance, created, **kwargs):
        if created:
            Owner.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_owner(sender, instance, **kwargs):
        instance.owner.save()

    def __str__(self):
        return self.user.username


class Bin(models.Model):
    title = models.CharField(max_length=100)
    products = models.ManyToManyField(
        'Product', related_name='bins', blank=True)

    owner = models.ForeignKey(
        Owner, related_name='owner_bins', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Product(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    shade = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    open_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    use_count = models.PositiveIntegerField(default=0)
    finish_date = models.DateField(null=True, blank=True)
    will_repurchase = models.BooleanField(default=False)
    image = models.URLField(max_length=200, null=True, blank=True)
    notes = models.TextField(blank=True)

    owner = models.ForeignKey(
        Owner, related_name='owner_products', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['brand', 'name']

    def __str__(self):
        return f'{self.name} by {self.brand}'
