"""
WSGI config for facultyForm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

#sys.path.append('/home/wsdcadmin/facultyForm')
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "facultyForm.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'facultyForm.settings'

application = get_wsgi_application()
