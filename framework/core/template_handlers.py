from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('framework', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


def render_template(template, **kwargs):
    return template.render(**kwargs).encode()