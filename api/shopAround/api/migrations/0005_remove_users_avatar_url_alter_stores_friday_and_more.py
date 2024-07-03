# Generated by Django 5.0.6 on 2024-07-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_stores_users_pricereport_favorite_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='avatar_url',
        ),
        migrations.AlterField(
            model_name='stores',
            name='friday',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='stores',
            name='monday',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='stores',
            name='saturday',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='stores',
            name='sunday',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='stores',
            name='thursday',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='stores',
            name='tuesday',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='stores',
            name='wednesday',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
