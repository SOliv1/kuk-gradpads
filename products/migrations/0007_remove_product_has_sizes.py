# Generated by Django 3.2.3 on 2021-05-16 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_merge_0004_auto_20210510_1312_0005_auto_20210512_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
    ]
