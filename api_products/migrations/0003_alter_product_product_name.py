# Generated by Django 4.2.3 on 2023-07-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_products', '0002_alter_product_category_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]