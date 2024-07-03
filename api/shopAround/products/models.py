from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    category_id = models.IntegerField()
    product_photo_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.product