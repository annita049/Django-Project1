# Generated by Django 5.1.1 on 2024-09-28 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_supplier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='proce',
            new_name='price',
        ),
    ]
