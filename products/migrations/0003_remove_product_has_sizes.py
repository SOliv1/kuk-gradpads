# Generated by Django 3.1.7 on 2021-04-30 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
    ]