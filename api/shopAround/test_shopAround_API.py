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

    response = api_client.get(ENDPOINT)
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
    assert len(response.json()) == 10


# def getProducts():
#     return requests.get(ENDPOINT)

@pytest.mark.django_db
def test_postProductRequest(api_client):
    payload = {
        "product": "test",
        "description": "test",
        "brand": "test",
        "size": "test",
        "product_photo_url": "test",
        "category": 1
    }
    response =  api_client.post(ENDPOINT, data=payload, format='json')
    print("response status code: ",response.status_code)
    print("The following product has been created: ", response.json())
    assert response.status_code == 201
    assert response.data == {
        "product_id": 11,
    	"product": "test",
        "description": "test",
        "brand": "test",
        "size": "test",
        "product_photo_url": "test",
        "category": 1
	}
    # deleteRequest(response.json()["product_id"])


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