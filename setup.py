import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Nano framework",
    version="dev",
    author="Andrei Etmanov",
    author_email="andres@space-coding.ru",
    description="This is not micro-, this is nano- framework!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ravique/otus-framework",
    py_modules={'wsgi'},
    packages=setuptools.find_packages(),
    install_requires=[
        'Jinja2==2.11.3',
    ],
    license="MIT",
)
