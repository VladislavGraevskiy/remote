import json

from django.http import JsonResponse
from django.shortcuts import redirect
from api.models import APIToken


def check_authorization(views):
    """
    Проверка авторизации пользователя
    :param views: 
    :return: 
    """

    def wrapper_check_authorization(request):
        if not request.user.is_authenticated:
            return redirect('/login')
        return views(request)

    return wrapper_check_authorization


def decorator_check_auth_token(handler_name):
    def check_auth_token(views):

        def wrapper_check_token(request):
            json_data = json.loads(request.body.decode())
            token_str = json_data.get('token', '').strip()
            try:
                if not token_str:
                    raise APIPermissionError
                try:
                    token = APIToken.objects.get(token=token_str)
                except APIToken.DoesNotExist:
                    raise APIPermissionError
                token_handlers = token.get_handlers()
                if handler_name not in token_handlers:
                    raise APIPermissionError
            except APIViewError:
                return JsonResponse({
                    'status': 'failed',
                    'massage': 'wrong token'
                },
                    status=401
                )

            return views(request)

        return wrapper_check_token
    return check_auth_token


class APIViewError(Exception):
    pass


class APIPermissionError(APIViewError):
    pass