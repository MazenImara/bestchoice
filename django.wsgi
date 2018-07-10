import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/var/www/bestchoice/env/lib/python3.6/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/bestchoice/bestchoice')
sys.path.append('/var/www/bestchoice/bestchoice/bestchoice')

os.environ['DJANGO_SETTINGS_MODULE'] = 'bestchoice.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/var/www/bestchoice/env/bin/activate_this.py")
#execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
