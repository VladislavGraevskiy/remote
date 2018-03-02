from django.http import JsonResponse
from django.shortcuts import render_to_response
# import requests
from django.views.decorators.csrf import csrf_exempt

from .forms.commands import Modes


def test_ground():
    # response = requests.get('http://0.0.0.0:8001/test_for_remote/').json()
    return JsonResponse('')


@csrf_exempt
def send_command(request):
    if request.POST:
        pass

    form = Modes()
    command = request.POST.get('command')
    return render_to_response('send_command.html', {'form': form})


@csrf_exempt
def main_page(requests):
    return render_to_response('main_page.html')


def sensors(requests):
    return render_to_response('sensors.html')