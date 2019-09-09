=============================
ecommerce_processors
=============================

.. image:: https://badge.fury.io/py/ecommerce_processors.svg
    :target: https://badge.fury.io/py/ecommerce_processors

.. image:: https://travis-ci.org/sodaling/ecommerce_processors.svg?branch=master
    :target: https://travis-ci.org/sodaling/ecommerce_processors

.. image:: https://codecov.io/gh/sodaling/ecommerce_processors/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sodaling/ecommerce_processors

processors for ecommerce

Documentation
-------------

The full documentation is at https://ecommerce_processors.readthedocs.io.

Quickstart
----------

Install ecommerce_processors::

    pip install ecommerce_processors

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'ecommerce_processors.apps.EcommerceProcessorsConfig',
        ...
    )

Add ecommerce_processors's URL patterns:

.. code-block:: python

    from ecommerce_processors import urls as ecommerce_processors_urls


    urlpatterns = [
        ...
        url(r'^', include(ecommerce_processors_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
