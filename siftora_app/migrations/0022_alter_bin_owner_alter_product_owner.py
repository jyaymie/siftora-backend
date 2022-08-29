# Generated by Django 4.0.6 on 2022-08-29 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siftora_app', '0021_member_bin_owner_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_bins', to='siftora_app.member'),
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_products', to='siftora_app.member'),
        ),
    ]
