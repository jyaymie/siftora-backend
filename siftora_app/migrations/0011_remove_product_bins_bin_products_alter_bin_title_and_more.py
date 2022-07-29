# Generated by Django 4.0.6 on 2022-07-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siftora_app', '0010_alter_bin_title_alter_product_brand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bins',
        ),
        migrations.AddField(
            model_name='bin',
            name='products',
            field=models.ManyToManyField(blank=True, to='siftora_app.product'),
        ),
        migrations.AlterField(
            model_name='bin',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='finish',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='shade',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]