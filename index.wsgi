import sae
from Lab4 import wsgi

application=sae.create_wsgi_app(wsgi.application)
