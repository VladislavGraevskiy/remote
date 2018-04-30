import string

from remote import settings


def form_response():
    return ''


def add_auth_token(json_data: dict) -> dict:
    json_data['token'] = settings.BSU_GROUND_TOKEN

    return json_data


def forming_command_data(cmd, arg='', device='', system='', time_of_execution=''):
    data = {
        'cmd': cmd,
        'system': 1,
    }
    if arg:
        data['arg'] = arg
    if device:
        data['device'] = device
    if system:
        data['system'] = system
    if time_of_execution:
        data['time_of_execution'] = time_of_execution

    final_json = add_auth_token({'data': data})

    return final_json
