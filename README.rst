===============================
Traversable Dict
===============================

.. image:: https://badge.fury.io/py/t_dict.png
    :target: http://badge.fury.io/py/t_dict

.. image:: https://travis-ci.org/vandersonmota/t_dict.png?branch=master
        :target: https://travis-ci.org/vandersonmota/t_dict

.. image:: https://pypip.in/d/t_dict/badge.png
        :target: https://pypi.python.org/pypi/t_dict


Traversing and Querying Dicts the easy way

* Free software: BSD license

Install
=======

.. code-block:: console

    pip install t_dict

Why?
--------

Dealing with deep nested dicts can be a total pain. TDict aims to make less boring working with it, using jsonpointer syntax for that.

It stand on the shoulders of jsonpointer (https://pypi.python.org/pypi/jsonpointer), which implements the RFC - https://tools.ietf.org/html/rfc6901


Usage
--------

.. code-block:: python

    from t_dict.t_dict import TDict

    td = TDict({'nested': { 'dict': 'here', 'other': {'spam': 'eggs'} }})
    td.find('/nested/dict')
    >> 'here'
    td.find('/nested/notfound', 'defaultvalue')
    >> 'defaultvalue'

    td.setin('/nested/dict', 'new')
    td['nested']['dict'] == 'new'
    >> True

    # converts dict to TDict
    isinstance(td.find('/nested/other'), TDict)
    >> True
