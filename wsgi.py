from framework.urls import urls
from framework.core.error_handlers import forbidden_handler, not_found_handler
from typing import List


def normalize_url(url: str) -> str:
    """
    Trim leading slash if exist and path is not root path
    """
    if url[-1] == '/' and url != '/':
        url = url[:-1]
        return url
    return url


def encode_response(response: str) -> List[bytes]:
    if isinstance(response, bytes):
        return [response]
    return [response.encode()]


class App:
    def __call__(self, request, start_response):
        url = normalize_url(request['REQUEST_URI'])

        if url in urls.keys():
            if request['REQUEST_METHOD'] not in urls[url].get('allowed_methods', []):
                return encode_response(forbidden_handler(request, start_response))

            start_response('200 OK', [('Content-Type', 'text/html')])
            view = urls[url]['view']
            return encode_response(view(request))

        else:
            return encode_response(not_found_handler(request, start_response))


app = App()
