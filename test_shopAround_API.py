ENDPOINT = "http://127.0.0.1:8000/api/products/"

import pytest
import requests
# from xprocess import ProcessStarter

# @pytest.fixture
# def myserver(xprocess):
#     class Starter(ProcessStarter):
#         # startup pattern
#         pattern = "PATTERN"

#         # command to start process
#         args = ['command', 'arg1', 'arg2']

#     # ensure process is running and return its logfile
#     logfile = xprocess.ensure("myserver", Starter)

#     conn = # create a connection or url/port info to the server
#     yield conn

#     # clean up whole process tree afterwards
#     xprocess.getinfo("myserver").terminate()


# @pytest.mark.xfail
# def test_getRequest():
#     response = requests.get(ENDPOINT)
#     # print("this is a response: ", response.json()[0]) 
#     # print("this is the response status code: ", response.status_code) 

#     desiredResult = [
#     {
#         "product_id": 1,
#         "product": "Apple",
#         "description": "Fresh red apples",
#         "brand": "FreshFarms",
#         "size": "1kg",
#         "product_photo_url": "http://example.com/apple.jpg",
#         "category": 1
#     },
#     {
#         "product_id": 2,
#         "product": "Banana",
#         "description": "Organic bananas",
#         "brand": "GreenEarth",
#         "size": "1kg",
#         "product_photo_url": "http://example.com/banana.jpg",
#         "category": 1
#     },
#     {
#         "product_id": 3,
#         "product": "Carrot",
#         "description": "Crunchy carrots",
#         "brand": "VeggieDelight",
#         "size": "1kg",
#         "product_photo_url": "http://example.com/carrot.jpg",
#         "category": 2
#     },
#     {
#         "product_id": 4,
#         "product": "Broccoli",
#         "description": "Fresh broccoli",
#         "brand": "VeggieDelight",
#         "size": "500g",
#         "product_photo_url": "http://example.com/broccoli.jpg",
#         "category": 2
#     },
#     {
#         "product_id": 5,
#         "product": "Milk",
#         "description": "Whole milk",
#         "brand": "DairyPure",
#         "size": "1L",
#         "product_photo_url": "http://example.com/milk.jpg",
#         "category": 3
#     },
#     {
#         "product_id": 6,
#         "product": "Cheese",
#         "description": "Cheddar cheese",
#         "brand": "DairyPure",
#         "size": "200g",
#         "product_photo_url": "http://example.com/cheese.jpg",
#         "category": 3
#     },
#     {
#         "product_id": 7,
#         "product": "Orange Juice",
#         "description": "Fresh orange juice",
#         "brand": "JuiceWorld",
#         "size": "1L",
#         "product_photo_url": "http://example.com/oj.jpg",
#         "category": 4
#     },
#     {
#         "product_id": 8,
#         "product": "Cola",
#         "description": "Soft drink",
#         "brand": "ColaCo",
#         "size": "1.5L",
#         "product_photo_url": "http://example.com/cola.jpg",
#         "category": 4
#     },
#     {
#         "product_id": 9,
#         "product": "Chips",
#         "description": "Potato chips",
#         "brand": "Snacky",
#         "size": "200g",
#         "product_photo_url": "http://example.com/chips.jpg",
#         "category": 5
#     },
#     {
#         "product_id": 10,
#         "product": "Cookies",
#         "description": "Chocolate chip cookies",
#         "brand": "Snacky",
#         "size": "300g",
#         "product_photo_url": "http://example.com/cookies.jpg",
#         "category": 5
#     }
#     {
#         "product": "test",
#         "description": "test",
#         "brand": "test",
#         "size": "test",
#         "product_photo_url": "test",
#         "category": 1
#     }
# ]  
#     assert response.status_code == 200
#     assert response.json() == desiredResult


def test_postProductRequest():
    payload = {
        "product": "test",
        "description": "test",
        "brand": "test",
        "size": "test",
        "product_photo_url": "test",
        "category": 1
    }
    response = requests.post(ENDPOINT, json=payload)
    print(response.json())
    print(response.status_code)


