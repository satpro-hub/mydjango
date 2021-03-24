#!/bin/bash
source /var/www/html/env/bin/activate
exec gunicorn  -c "/var/www/html/myproject/gunicorn_config.py" myproject.wsgi
