import csv
from django.core.management.base import BaseCommand
from api.models import Stores, Categories,Products,Users,Favorite_Products,PriceReport

class Command(BaseCommand):
    help = 'seeding database'
    def handle(self, *args, **kwargs):
        self.seed_stores()
        self.seed_categories()
        self.seed_products()
        self.seed_users()
        self.seed_favorite_products()
        self.seed_priceReports()
        self.stdout.write(self.style.SUCCESS('Data successfully seeded'))



    def seed_stores(self):
        with open('stores.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Stores.objects.create(**row)

    def seed_categories(self):
        with open('categories.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Categories.objects.create(**row)

    def seed_products(self):
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Products.objects.create(**row)


    def seed_users(self):
        with open('users.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Users.objects.create(**row)

    
    def seed_favorite_products(self):
        with open('favproducts.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Favorite_Products.objects.create(**row)


    def seed_priceReports(self):
        with open('pricereports.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                PriceReport.objects.create(**row)