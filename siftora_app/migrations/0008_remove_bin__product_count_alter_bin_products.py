# Generated by Django 4.0.6 on 2022-07-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siftora_app', '0007_bin__product_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bin',
            name='_product_count',
        ),
        migrations.AlterField(
            model_name='bin',
            name='products',
            field=models.ManyToManyField(blank=True, to='siftora_app.product'),
        ),
    ]
