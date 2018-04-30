from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from remote_control.models.models import Request, Response


def test(request):
    response_message = {
        'status': 'success',
    }
    return JsonResponse(response_message)


@csrf_exempt
def answer(request):
    json_data = json.loads(request.body.decode())
    cid = json_data['data']['cid']
    answer = json_data['data']['raw_data']

    request_obj = Request.objects.filter(cid=str(cid))[0]
    print(request_obj)
    Response.objects.create(response_body=answer, request=request_obj)

    print(json_data)
    if request.POST:
       print(request)

    return JsonResponse({'status': 'ok'})