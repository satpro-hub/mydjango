command = '/var/www/html/env/bin/gunicorn'
pythonpath = '/var/www/html/myproject'
bind = '0.0.0.0:8000'
workers = 5
user = 'www-data'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=myproject.settings'
