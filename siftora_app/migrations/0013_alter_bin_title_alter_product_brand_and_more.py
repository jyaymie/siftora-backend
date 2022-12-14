# Generated by Django 4.0.6 on 2022-07-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siftora_app', '0012_alter_bin_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='finish',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='shade',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
