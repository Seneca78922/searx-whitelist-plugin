#domain filter plugin
from setuptools import setup

GIT_URL = 'https://github.com/Seneca78922/searx-whitelist-plugin'

setup(
    name='searx-whitelist-plugin',
    version='0.1.0',
    description='SearxNG plugin to filter search results based on trusted domains',
    url=GIT_URL,
    py_modules=[
        'trusted_domains_filter',
    ],
    entry_points={
        'searxng.plugins': [
            'trusted-domains-filter = trusted_domains_filter'
        ]
    },
)