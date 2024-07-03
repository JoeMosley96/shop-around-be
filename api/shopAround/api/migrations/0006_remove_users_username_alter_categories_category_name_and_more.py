# Generated by Django 5.0.6 on 2024-07-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_users_avatar_url_alter_stores_friday_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
        migrations.AlterField(
            model_name='categories',
            name='category_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterModelTable(
            name='favorite_products',
            table='favourite_products',
        ),
        migrations.AlterModelTable(
            name='pricereport',
            table='price_reports',
        ),
        migrations.AlterModelTable(
            name='stores',
            table='stores',
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]
