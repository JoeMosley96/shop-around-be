# ShopAround
ShopAround is a mobile application designed to compare prices of products in local shops, helping users find the cheapest options in their area. The app provides functionalities to search for products, find nearby stores, manage favourite items, and browse products by category.

Front end repo available here:
https://github.com/JoeMosley96/shop-around-fe

Features

- Go Shopping: Find the cheapest price for a desired product within a specified radius from your current location.
- Get Local Stores: View all stores within a given radius from your current location.
- Report Price: Report the price paid for a product and where it was bought.
- Get Favourites: Manage and view a list of favourite products.

Tech Stack
- Backend: Python, Django, Django REST Framework, PostgreSQL with PostGIS extension
- Frontend: JavaScript, React Native, Tailwind CSS, Google Maps API, Expo
- Testing: Pytest

Backend Setup

1) Clone the repository:
```
git clone https://github.com/JoeMosley96/shop-around-be.git
```
2) Navigate to directory
```
shop-around-be
```
3) Create a virtual environment and activate it:
```
pipenv shell
```
4) Install the dependencies:
```
pipenv install
```
5) Configure the database:
```
source setenv.sh test
```
6) Apply migrations and seed:
```
python manage.py migrate
```
```
python manage.py seed
```
7) Run the development server:
```
python manage.py runserver
```
Usage
To use the application.........

API Endpoints

Available endpoints + descriptions can be viewed in the endpoints.json file

Running Tests
To run the tests for the API endpoints and other functionalities:

Ensure your virtual environment is activated and cd into the appropriate directory:
    - /shop-around-be/api/shopAround#

Run the tests using pytest and view a summary of the tests:

pytest -rP
