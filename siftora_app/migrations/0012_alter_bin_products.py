# Generated by Django 4.0.6 on 2022-07-28 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siftora_app', '0011_remove_product_bins_bin_products_alter_bin_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='products', to='siftora_app.product'),
        ),
    ]
