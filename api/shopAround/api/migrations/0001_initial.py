# Generated by Django 5.0.6 on 2024-07-03 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=255)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=13)),
                ('lon', models.DecimalField(decimal_places=10, max_digits=13)),
                ('monday', models.CharField(blank=True, max_length=300)),
                ('tuesday', models.CharField(blank=True, max_length=300)),
                ('wednesday', models.CharField(blank=True, max_length=300)),
                ('thursday', models.CharField(blank=True, max_length=300)),
                ('friday', models.CharField(blank=True, max_length=300)),
                ('saturday', models.CharField(blank=True, max_length=300)),
                ('sunday', models.CharField(blank=True, max_length=300)),
            ],
            options={
                'db_table': 'stores',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('brand', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=50)),
                ('product_photo_url', models.CharField(blank=True, max_length=500, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categories')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='PriceReport',
            fields=[
                ('price_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.products')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stores')),
            ],
            options={
                'db_table': 'price_reports',
            },
        ),
        migrations.CreateModel(
            name='Favorite_Products',
            fields=[
                ('fav_product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
            options={
                'db_table': 'favourite_products',
            },
        ),
    ]
