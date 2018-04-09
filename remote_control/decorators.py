from django.shortcuts import redirect


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


