# Generated by Django 4.0.6 on 2022-07-29 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siftora_app', '0013_alter_bin_title_alter_product_brand_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bin',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]
