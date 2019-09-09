=====
Usage
=====

To use ecommerce_processors in a project, add it to your `INSTALLED_APPS`:

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
