# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.0.1] - 2025-06-12

- Fix function get_page_placeholders.

## [3.0.0] - 2025-06-05

- Upgrade to python >= 3.10 and django-cms 4.1.

## [2.0.3] - 2025-01-27

* Fix ImportError: lxml.html.clean module is now a separate project lxml_html_clean.

## [2.0.2] - 2024-07-17

* Fix for py312: Use LooseVersion from looseversion instead of distutils.
* Fix tag links in CHANGELOG.

## [2.0.1] - 2023-10-16

* Fix get_plugin_index_data in helpers.py for
  - AccordionItemRenderMixin.render in djangocms_frontend/contrib/accordion/frameworks/bootstrap5.py.
  - TabItemRenderMixin.render in djangocms_frontend/contrib/tabs/frameworks/bootstrap5.py.

## [2.0.0] - 2023-07-18

* Update code to python >= 3.7 and Django > 3.2.

## [1.1.0] - 2020-02-20

* Added support for Django 2.2 and django CMS 3.7
* Added support for Transifex
* Added isort and flake8
* Changed from djangocms-helper to django-app-helper
* Extended test matrix
* Adapted code base to align with other supported addons
* Removed ``INDEX_TITLE`` backwards compatibility shim


## [1.0.1] - 2018-06-14

* Added support for configurable alias from language function
  with the new ``ALDRYN_SEARCH_ALIAS_FROM_LANGUAGE`` setting


## [1.0.0] - 2018-04-05

* Added django CMS 3.5 to test matrix
* Dropped support for Django < 1.8
* Dropped suppport for django CMS < 3.2


## [0.5.0] - 2018-03-06

* Added new ``ALDRYN_SEARCH_EXCLUDED_PLUGINS`` setting to prevent
  specific plugin types from being indexed


## [0.4.1] - 2017-11-02

* Updated metadata for pypi


## [0.4.0] - 2017-10-20

* Added CMS 3.5.x compatibility
* Dropped support for Django 1.7.x


## [0.3.0] - 2016-10-20

* Added CMS 3.4.x compatibility
* Added Django 1.8.x compatibility


## [0.2.12] - 2016-05-19

* Added CMS 3.3.x compatibility


## [0.2.11] - 2016-02-03

* Added Django 1.9 compatibility
* Dropped support for django CMS 2.4
* Fixed Travis setup
* Fixed importlib deprecation warning
* Fixed bug where unpublishing cms page would not remove it from index
* Added support for explicit signal based indexing
* Fixed regression on plugin indexing
* Restored the old _strip_tags due to a regression


## [0.2.10] - 2015-10-15

* Updated documentation
* Added Django 1.8 compatibility


## [0.2.9] - 2015-08-05

* Tests
* Fixed issue with lxml parser error


## [0.2.8] - 2015-07-06

* Fixed issues with strip_tags
* Fixed issue where the non-public version of a title was being indexed


## [0.2.7]  - 2015-04-16

* Fixed a issue with get_language return wrong language in indexing


## [0.2.6] - 2015-01-27

* Fixed issue with search_fields not following relationships


## [0.2.5] - 2015-01-27

* Fixed issue with javascript not being stripped correctly
* Fixed duplicate content issue when indexing a plugin that set search_fields


## [0.2.4] 2014-11-24

* Added missing requirements to setup.py (issue #23)
* Added for_write router. Fixes issues on single object updates


## [0.2.3] - 2014-09-30

* Fixed TypeError when rebuilding page index on cms 2.4
* Fixed typo on README
* Fixed a bug on spelling suggestion check when using pagination


## [0.2.2] - 2014-08-06

* Fixed bug in get_model_path utility (issue #19)


## [0.2.1] - 2014-07-25

* Fixed bug in form handling on search view


## [0.2.0] - 2014-07-24

* Removed contrib.pagination.DiggPaginator (use aldryn_common.paginator.DiggPaginator)
* Added alias_from_language utility function
* Renamed searchqueryset to search_queryset in search view
* Added search_queryset_class to search view

* Added helpers module
* Added helper function get_plugin_index_data
* Added new utility clean_join
* Added models attribute on view, to limit search by specific models
* Renamed get_request_for_search to get_request and moved it to helpers module
* Added get_request_instance method to base index, this allows adding custom attributes to request object
* Renamed INDEX_TITLE to index_title to keep the same format as haystack
* Refactored plugin data indexing to split on whitespace, thus reducing index size


## [0.1.9] - 2014-05-17
## [0.1.8] - 2014-05-16
## [0.1.7] - 2014-03-20
## [0.1.6] - 2014-01-30
## [0.1.5] - 2014-01-29
## [0.1.4] - 2014-01-29
## [0.1.3] - 2013-11-11
## [0.1.2] - 2013-08-07

[unreleased]: https://github.com/CZ-NIC/djangocms-aldryn-search/compare/3.0.1...master
[3.0.1]: https://github.com/CZ-NIC/djangocms-aldryn-search/compare/3.0.0...3.0.1
[3.0.0]: https://github.com/CZ-NIC/djangocms-aldryn-search/compare/2.0.3...3.0.0
[2.0.3]: https://github.com/CZ-NIC/djangocms-aldryn-search/compare/2.0.2...2.0.3
[2.0.2]: https://github.com/CZ-NIC/djangocms-aldryn-search/compare/2.0.1...2.0.2
[2.0.1]: https://github.com/CZ-NIC/djangocms-aldryn-search/compare/2.0.0...2.0.1
[2.0.0]: https://github.com/CZ-NIC/djangocms-aldryn-search/compare/1.1.0...2.0.0
[1.1.0]: https://github.com/divio/aldryn-search/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/divio/aldryn-search/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/divio/aldryn-search/compare/0.5.0...1.0.0
[0.5.0]: https://github.com/divio/aldryn-search/compare/0.4.1...0.5.0
[0.4.1]: https://github.com/divio/aldryn-search/compare/0.4.0...0.4.1
[0.4.0]: https://github.com/divio/aldryn-search/compare/0.3.0...0.4.0
[0.3.0]: https://github.com/divio/aldryn-search/compare/0.2.12...0.3.0
[0.2.12]: https://github.com/divio/aldryn-search/compare/0.2.11...0.2.12
[0.2.11]: https://github.com/divio/aldryn-search/compare/0.2.10...0.2.11
[0.2.10]: https://github.com/divio/aldryn-search/compare/0.2.9...0.2.10
[0.2.9]: https://github.com/divio/aldryn-search/compare/0.2.8...0.2.9
[0.2.8]: https://github.com/divio/aldryn-search/compare/0.2.7...0.2.8
[0.2.7]: https://github.com/divio/aldryn-search/compare/0.2.6...0.2.7
[0.2.6]: https://github.com/divio/aldryn-search/compare/0.2.5...0.2.6
[0.2.5]: https://github.com/divio/aldryn-search/compare/0.2.4...0.2.5
[0.2.4]: https://github.com/divio/aldryn-search/compare/0.2.3...0.2.4
[0.2.3]: https://github.com/divio/aldryn-search/compare/0.2.2...0.2.3
[0.2.2]: https://github.com/divio/aldryn-search/compare/0.2.1...0.2.2
[0.2.1]: https://github.com/divio/aldryn-search/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/divio/aldryn-search/compare/0.1.9...0.2.0
[0.1.9]: https://github.com/divio/aldryn-search/compare/0.1.8...0.1.9
[0.1.8]: https://github.com/divio/aldryn-search/compare/0.1.6...0.1.8
[0.1.7]: https://github.com/divio/aldryn-search/compare/0.1.5...0.1.7
[0.1.6]: https://github.com/divio/aldryn-search/compare/0.1.5...0.1.6
[0.1.5]: https://github.com/divio/aldryn-search/compare/0.1.4...0.1.5
[0.1.4]: https://github.com/divio/aldryn-search/compare/0.1.3...0.1.4
[0.1.3]: https://github.com/divio/aldryn-search/compare/0.1.2...0.1.3
[0.1.2]: https://github.com/divio/aldryn-search/releases/tag/0.1.2
