# Generated by Django 5.0.6 on 2024-11-23 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_alter_product_is_biodegradable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
