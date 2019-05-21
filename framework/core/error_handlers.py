from framework.core.error_views import forbidden_view, not_found_view
from framework.urls import urls


def forbidden_handler(request, start_response):
    url = request['REQUEST_URI']
    start_response('403 FORBIDDEN', [('Content-Type', 'text/html')])
    return forbidden_view(request,
                          context={'request_method': request['REQUEST_METHOD'],
                                   'allowed_methods': urls[url].get('allowed_methods')})


def not_found_handler(request, start_response):
    start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
    return not_found_view(request)
