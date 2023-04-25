import logging
import requests 
import os



from flask_babel import gettext
try: 
     from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse


name = gettext('Only show results from trusted domains')
description = gettext('filters all results not matching domain (and its subpages)')
default_on = False
preference_section = 'general'


allowed_domains = ['developer.mozilla.org', 'javascript.info', 'wikipedia.org', 'w3.org',
                   'developers.google.com',]


def is_domain_allowed(url):
    domain = urlparse(url).netloc
    allowed = any(allowed_domain in domain for allowed_domain in allowed_domains)
    return allowed

def post_search(request, search):
    filtered_results = [
        result for result in list(search.result_container._merged_results)
        if is_domain_allowed(result.get('url'))
    ]
    search.result_container._merged_results = filtered_results