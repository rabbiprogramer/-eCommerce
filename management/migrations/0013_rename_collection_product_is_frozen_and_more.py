# Generated by Django 5.0.6 on 2024-12-08 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_rename_is_frozen_product_collection_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='collection',
            new_name='is_frozen',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sell_price',
            new_name='sale_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount_percentage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_available',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='session_key',
        ),
        migrations.RemoveField(
            model_name='product',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='product',
            name='variants',
        ),
        migrations.AddField(
            model_name='product',
            name='add_stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.JSONField(blank=True, help_text="Product's extra attributes like size, color, etc.", null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='management.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='collections',
            field=models.ManyToManyField(blank=True, related_name='products', to='management.collection'),
        ),
        migrations.AddField(
            model_name='product',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='global_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(default=1, upload_to='product_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='is_biodegradable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_fragile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='max_temperature',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_id_type',
            field=models.CharField(choices=[('ISBN', 'ISBN'), ('UPC', 'UPC'), ('EAN', 'EAN'), ('JAN', 'JAN')], default='ISBN', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='restock_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='selected_countries',
            field=models.ManyToManyField(blank=True, related_name='products_in_country', to='management.country'),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_method',
            field=models.CharField(choices=[('seller', 'Fulfilled by Seller'), ('admin', 'Fulfilled by Admin')], default='admin', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='management.brand'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='regular_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='management.vendor'),
        ),
    ]