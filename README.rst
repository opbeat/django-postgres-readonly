django-postgres-readonly
========================

A readonly database backend for Django and PostgreSQL. It does this by setting
the connection to "readonly".


Usage
-----

To configure a read-only database connection, add an entry to your ``DATABASES``
setting that uses `django_postgres_readonly` as the engine::

    DATABASES = {
        'default': {
            'NAME': 'my_django_db',
            'ENGINE': 'django.db.backends.postgresql',
            'USER': 'my_db_user',
            'PASSWORD': 'my_password'
        },
        'readonly': {
            'NAME': 'my_django_db',
            'ENGINE': 'django_postgres_readonly',
            'USER': 'my_db_user',
            'PASSWORD': 'my_password'
        }
    }


Caveats
-------

This backend is not meant to provide security against willful bad actors. Its
main reason of existence is to protect you against your own mistakes.

If you need secure way for read-only connections, you should probably
look into creating a separate user and grant it ``SELECT`` rights only.
