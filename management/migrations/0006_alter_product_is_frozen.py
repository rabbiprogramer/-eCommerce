# Generated by Django 5.0.6 on 2024-11-23 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_frozen',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]