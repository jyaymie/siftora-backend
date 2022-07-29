# Generated by Django 4.0.6 on 2022-07-29 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siftora_app', '0015_product_bins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bins',
        ),
        migrations.AlterField(
            model_name='bin',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='bins', to='siftora_app.product'),
        ),
    ]
