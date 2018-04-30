import requests

from remote import settings
from third_party.bsu_ground.utils import add_auth_token


def send_command_to_api(json_data):
    path = '/default/commands/'
    end_url = settings.BSU_GROUND_URL + path

    json_data = add_auth_token(json_data)

    # TODO: вернуть как было
    response = requests.post(end_url, json=json_data, timeout=10)
    json_response = response.json()
    # json_response = {
    #     'data': {
    #         'cid': 391930
    #     }
    # }

    return json_response
