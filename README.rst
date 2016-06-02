slumbercache
============

Slumber is a Python library that provides a convenient yet powerful
object-oriented interface to ReSTful APIs. It acts as a wrapper around the
excellent requests_ and abstracts away the handling of URLs, serialization,
and request processing.

.. _requests: http://python-requests.org/


Install
=======
``pip install slumbercache``


Usage
=====

Example Usage with Cache enabled

.. code-block:: pycon

    import slumbercache
    
    api = slumbercache.API("http://slumbercache.in/api/v1/", auth=("demo", "demo"), cache=True)
    ## GET http://slumbercache.in/api/v1/note/
    api.note.get()


Credit
======

`slumbercache` is a fork of slumber_ with Cache added for better performance

.. _slumber: https://github.com/samgiles/slumber




