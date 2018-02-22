from django.http import JsonResponse
import requests


def test_ground():
    response = requests.get('http://0.0.0.0:8001/test_for_remote/').json()
    return JsonResponse(response)
