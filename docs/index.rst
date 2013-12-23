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

 - Support multiple accounts.
 - Retrieve all the available Groups, Categories and Reports.
 - Limit the number of reports to retrieve, also, you can filter for category or dates.
 - Create new reports.
 - Support for proxies. You can find more details in the :ref:`examples` section.

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
