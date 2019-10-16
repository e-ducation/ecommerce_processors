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

## 记录
https://github.com/e-ducation/ecommerce

目前来说，这个django_app装上后，在ecommerce的setting的processor_list添加对应的后，可以摸到并且得以运行的。但是无法脱离我们的ecommerce运行,原因如下：

1.ecommerce/extensions/basket/views.py,这个是购物车的view页面，做了大量的修改。如加入了微信的二维码链接返回等数据。也就是说，如果要使用微信processor，我们绕不开要修改原来购物车的view的。我这段时间想办法用用我们的app来覆盖url来导向我们的view。但是发现还是不行。出现了静态和翻译资源调用错误等问题。这个问题得慢慢摸着静态资源一个个排错。。我承认我排着排着不耐烦。。然后划水了

2.大量支付宝和微信的静态资源我尝试迁移出来，但是发现迁出来后还得改对应的路径。。不太成功。

3.还有一点，就是tutor那边，ecommerce不能像edx一样做plugin自动加载。以为着我如果装这个app的话，必须得在django的install_app那里加这个app，不然一堆reverse都摸不到。

总结来说，processor是隔出来了，但是无法脱离我们的ecommerce。
