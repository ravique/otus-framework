from framework.urls import urls
from framework.core.error_handlers import forbidden_handler, not_found_handler


def normalize_url(url: str) -> str:
    if url[-1] == '/' and url != '/':
        url = url[:-1]
        return url
    return url


class App:
    def __call__(self, request, start_response):
        url = normalize_url(request['REQUEST_URI'])

        if url in urls.keys():
            if request['REQUEST_METHOD'] not in urls[url].get('allowed_methods', []):
                return forbidden_handler(request, start_response)

            start_response('200 OK', [('Content-Type', 'text/html')])
            view = urls[url]['view']
            return view(request)

        else:
            return not_found_handler(request, start_response)


app = App()
