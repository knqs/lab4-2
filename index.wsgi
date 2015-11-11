import sae
from library import wsgi

application=sae.create_wsgi_app(wsgi.application)
