# Generated by Django 4.2.7 on 2023-12-14 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_rent',
            name='return_date',
            field=models.DateField(auto_now=True),
        ),
    ]