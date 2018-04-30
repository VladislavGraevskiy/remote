from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from remote_control.decorators import decorator_check_auth_token
from remote_control.models.models import Request, Response, RawData


def test(request):
    response_message = {
        'status': 'success',
    }
    return JsonResponse(response_message)


@csrf_exempt
@decorator_check_auth_token('telemetry')
def telemetry(request):
    if request.body:
        json_data = json.loads(request.body.decode())
        telemetry_data = json_data.get('data')
        RawData.objects.create(raw_data=telemetry_data)

    return JsonResponse({'status': 'ok'})


@csrf_exempt
@decorator_check_auth_token('answer')
def answer(request):
    return_json = {
        'status': 'ok'
    }
    if request.body:
        json_data = json.loads(request.body.decode())

        answer_data = json_data.get('data', {})
        cid = answer_data.get('cid')
        answer_raw_data = answer_data.get('raw_data')

        if cid and answer_data:
            request_obj = Request.objects.filter(cid=str(cid))[0]
            try:
                Response.objects.create(
                    response_body=answer_raw_data, request=request_obj
                )
            except IntegrityError:
                return_json = {
                    'status': 'failed',
                    'message': 'response to request already exists'
                }
        else:
            return_json = {
                'status': 'failed',
                'message': 'wrong data'
            }

    return JsonResponse(data=return_json)
