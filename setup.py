# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from aldryn_search import __version__


REQUIREMENTS = [
    'lxml~=5.3',
    'lxml-html-clean~=0.4',
    'django-appconf~=1.1',
    'django-cms~=4.1',
    'djangocms-versioning~=2.3',
    'django-haystack~=3.3',
    'django-spurl~=0.6',
    'django-standard-form~=1.1',
    'djangocms-aldryn-common~=2.0',
    'looseversion~=1.3',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Framework :: Django',
    'Framework :: Django :: 4.0',
    'Framework :: Django :: 5.0',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
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
    python_requires='>=3.10',
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    # test_suite='tests.settings.run',
)
