from django.shortcuts import render
from django.http import JsonResponse
import importlib.resources
import json

def index(request):
    with importlib.resources.open_text("api", "endpoints.json") as file:
        data = json.load(file)

    return JsonResponse(data)