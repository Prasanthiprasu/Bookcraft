# Generated by Django 4.2.7 on 2023-12-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20231128_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
