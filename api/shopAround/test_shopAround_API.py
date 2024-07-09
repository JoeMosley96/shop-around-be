ENDPOINT = "http://127.0.0.1:8000/api/products/"

import os
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
import pytest
import requests

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_get_products(api_client):
    url=reverse('api/products/')

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0] == {
		"product_id": 1,
		"product": "Apple",
		"description": "Fresh red apples",
		"brand": "FreshFarms",
		"size": "1kg",
		"product_photo_url": "http://example.com/apple.jpg",
		"category": 1
	}

# @pytest.mark.django_db
# def test_getRequest():
#     response = requests.get(ENDPOINT)
#     print(f"Recieved {len(response.json())} items")
#     assert len(response.json()) == 10
#     assert response.status_code == 200 

# def getProducts():
#     return requests.get(ENDPOINT)

# @pytest.mark.django_db
# def test_postProductRequest():
#     payload = {
#         "product": "test",
#         "description": "test",
#         "brand": "test",
#         "size": "test",
#         "product_photo_url": "test",
#         "category": 1
#     }
#     response = requests.post(ENDPOINT, json=payload)
#     print("response status code: ",response.status_code)
#     print("The following product has been created: ", response.json())
#     assert response.status_code == 201
#     # deleteRequest(response.json()["product_id"])


# def createEntry():
#     payload = {
#     "product": "test",
#     "description": "test",
#     "brand": "test",
#     "size": "test",
#     "product_photo_url": "test",
#     "category": 1
#     }
#     return requests.post(ENDPOINT, json=payload)


# def test_postDeleteRequest():
#     createResponse = createEntry().json()
#     print("The following product has been created: ", createResponse)
#     product_id = createResponse["product_id"]
#     # product_id = 89
    
#     deleteResponse = requests.delete(ENDPOINT + str(product_id))
#     print("Delete response status code: ",deleteResponse.status_code)
#     if deleteResponse.status_code == 204 :
#         print(f"Product {product_id} has successfully been deleted")
#     assert deleteResponse.status_code == 204
#     assert len(getProducts().json()) == 10

# def deleteRequest(product_id):
#     return requests.delete(ENDPOINT + str(product_id))