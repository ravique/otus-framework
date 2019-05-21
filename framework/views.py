from framework.core.template_handlers import env, render_template


# create your views here :)

def base_view(request, **kwargs):
    return [b'Hello, OTUS']


def mainpage_view(request, **kwargs):
    request_method = request['REQUEST_METHOD']
    template = env.get_template('index.html')
    return [render_template(template, h1='Mainpage', request_method=request_method)]


def books_list_view(request, **kwargs):
    return [b'Books List']


def disks_list_view(request, **kwargs):
    return [b'Disks List']