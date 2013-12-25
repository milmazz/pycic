.. pycic documentation master file, created by
   sphinx-quickstart on Mon Dec 23 07:56:59 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pycic: Python client for CIC_
=============================

``pycic`` is an MIT_ licensed client, written in Python, that lets you interact with the CIC_ (Centro de Integración Ciudadana) API.

``pycic`` currently works with the ``nl`` and ``sal`` accounts. You might notice that ``nl`` is the default account, but you can change quickly that behavior at the moment of the instance creation, for example: ``Report(account="sal")``.

Feature support
+++++++++++++++

 - Supports multiple accounts.
 - Retrieves all the available Groups, Categories and Reports.
 - Limits the number of reports to retrieve, also, you can filter for category or dates.
 - Creates new reports.
 - Supports for proxies. You can find more details in the :ref:`examples` section.
 - Are you asking yourself if ``pycic`` works with Python 3?, *Yes*, the following is a list of Python platforms that are officially supported:

   + Python 2.6
   + Python 2.7
   + Python 3.2
   + Python 3.3
   + PyPy

API Documentation
+++++++++++++++++

.. toctree::
   :maxdepth: 2

   report
   category
   group
   base
   exceptions

Examples
++++++++

.. toctree::
   :maxdepth: 2

   examples

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _CIC: http://cic.mx
.. _MIT: http://opensource.org/licenses/MIT
