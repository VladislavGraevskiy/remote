from django.http import JsonResponse


def test(request):
    response_message = {
        'status': 'success',
    }
    return JsonResponse(response_message)
