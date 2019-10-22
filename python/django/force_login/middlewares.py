from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.urls import reverse


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        LOGIN_URL = reverse('users:login')
        response = self.get_response(request)

        is_authenticated = bool(request.user) and bool(request.user.is_authenticated)
        is_not_login_url = request.path != LOGIN_URL

        if (not is_authenticated) and is_not_login_url:
            return HttpResponseRedirect(LOGIN_URL)

        return response
