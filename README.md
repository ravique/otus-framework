# Nano Framework

Very simple and tiny MTV-style, Django-(a little bit)-like web-framework. Allows to create web-pages (!!!) with Jinja2 template engine. Allowable HTTP-methods for every page can be chosen. 
Handles 404 and 403 pages.  
Distributed with example views and templates.

[== DEMO ==](http://otus.space-coding.com)

**<Attention!>** This module was made by mad-skilled student. Never use it in production. I said "NEVER". :) **</Attention!>**

## Install
### Easy install

To install this script using pip (auto install, requirements will be installed automatically):
```
$ pip install git+https://github.com/ravique/otus-framework.git
```

### Manual install

1. Download [Nano Framework](https://github.com/ravique/otus-framework/archive/master.zip) manually.

2. Install requirements:

```
$ pip install -r requirements.txt
```

Or install Jinja2 manually:

```
$ pip install Jinja2
```

### Prerequisites

You need to have configurated uWSGI-server.

**uwsgi.ini entry points:**

```
chdir = %path to wsgi.py%
module = wsgi:app
```

## Usage

To create a web-page you need:
- Create view function for your page in framework/views.py. Function must have first positional 
argument 'request' string.
**Example:**
```
def base_view(request, **kwargs):
    return [b'Hello, OTUS']
```
- Add routing rule 'urls' dict in framework/urls.py.  
**Example:**
```
'/': {'view': framework.views.mainpage_view, 'allowed_methods': ('GET', 'POST')},
```
Where:
`'/'` – internal url, 
`'view': framework.views.mainpage_view` - your view function, 
`'allowed_methods': ('GET', 'POST')` – HTTP-methods allowed for your page. If you pass no allowed methods there, 
page always will return 403 Forbidden.
- If you want, you can use Jinja2 template, create .html file in framework/templates. To use
template in your view function:
```
template = env.get_template('index.html')
return render_template(template)
```
You can pass variables from view to your template.  
**Example:**
```
render_template(template, foo='Foo', bar='Bar')
```

### Other features
- Default 404 page included. It will be shown if user will reach any page, not listed in 'urls' dict.
- Pages with leading slash and without it return the same content.

## Authors

* **Andrei Etmanov** - *Student of OTUS :)*

## License

This project is licensed under the MIT License – see the [LICENSE.md](LICENSE.md) file for details
