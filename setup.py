# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from aldryn_search import __version__


REQUIREMENTS = [
    'lxml',
    'lxml_html_clean',
    'django-appconf',
    'django-cms>=3.11',
    'django-haystack>=2.0.0',
    'django-spurl',
    'django-standard-form',
    'djangocms-aldryn-common',
    'looseversion',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Framework :: Django',
    'Framework :: Django :: 3.2',
    'Framework :: Django :: 4.0',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]


setup(
    name='djangocms-aldryn-search',
    version=__version__,
    author='Benjamin Wohlwend',
    author_email='piquadrat@gmail.com',
    url='https://github.com/CZ-NIC/djangocms-aldryn-search',
    license='BSD License',
    description='An extension to django CMS to provide multilingual Haystack indexes.',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    test_suite='tests.settings.run',
)
