################
Welcome to Gruvi
################

.. default-domain:: py

Gruvi is a network library for Python. It combines the efficiencies of
event-based I/O with a sequential programming model. Gruvi uses libuv_ (via
pyuv_) as the underlying, high-performance event-based I/O layer, and
greenlets_ to turn the callback programming style associated with event-based
I/O into a traditional sequential programming style. 

Gruvi is similar in concept to gevent_, concurrence_ and eventlet_. For a
rationale on why I've created a new library, see :ref:`rationale`.

Gruvi values:

* Performance. Gruvi's main dependencies, libuv and greenlet, have a very
  strong focus on performance and so does Gruvi itself. Gruvi also contains a
  very fast HTTP implementation based on the Joyent/Node.js event driven
  http-parser_.
* Scalability. Thanks to libuv and the low memory usage of greenlets, Gruvi can
  support hundreds of thousands of concurrent connections.
* Platform support. All supported platforms (Posix, Mac OSX and Windows) are
  first-class citizens. This is mostly thanks to libuv.
* Minimalistic design. All of Gruvi is less than 4,000 lines of Python.

Contents
########

.. toctree::
   :maxdepth: 1

   rationale
   install
   tutorial
   concepts
   reference
   changelog

Gruvi is free software, available under the MIT license.

The author of Gruvi may be contacted at geertj@gmail.com. You may also submit
tickets or suggenstions for improvements on Gruvi's `github page`_.

.. _libuv: https://github.com/joyent/libuv
.. _pyuv: http://pyuv.readthedocs.org/en/latest
.. _greenlets: http://greenlet.readthedocs.org/en/latest
.. _gevent: http://gevent.org/
.. _concurrence: http://opensource.hyves.org/concurrence
.. _eventlet: http://eventlet.net/
.. _http-parser: https://github.com/joyent/http-parser
.. _txdbus: https://github.com/cocagne/txdbus
.. _github page: https://github.com/geertj/gruvi