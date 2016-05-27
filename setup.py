from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-postgres-readonly',

    version='1.0.0',

    description='A backend for Django and Postgres that sets up a readonly connection',
    long_description=long_description,

    url='https://github.com/opbeat/django-postgres-readonly',

    author='Opbeat',
    author_email='benjamin@opbeat.com',

    license='BSD',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: BSD License',

        'Framework :: Django',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='django postgres',
    packages=find_packages(exclude=['tests']),

    install_requires=['Django', 'psycopg2'],

    extras_require={
        'test': ['coverage'],
    },
)