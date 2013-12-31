pycic: Python client for CIC_
=============================

.. image:: https://travis-ci.org/milmazz/pycic.png?branch=master
	:target: https://travis-ci.org/milmazz/pycic

 .. image:: https://coveralls.io/repos/milmazz/pycic/badge.png?branch=master
    :target: https://coveralls.io/r/milmazz/pycic?branch=master

``pycic`` is an MIT Licensed client, written in Python, that lets you interact with the CIC_ (Centro de Integracion Ciudadana) API. Hope that you enjoy it.

``pycic`` currently works with the ``nl`` (`Nuevo Leon`_) and ``sal`` (Saltillo_) accounts. *Nuevo Leon* is the default option,
but you can quickly change that behavior at the moment of the instance creation, for example: ``Report(account="sal")``

Right now you can get *groups*, *categories* and *reports* with ``pycic``. Also, you can create new reports, let's show you a bit this features:

Reports
+++++++

Get all the available reports

.. code-block:: pycon

    >>> from pycic.report import Report
    >>> r = Report()
    >>> r.get()
    {u'reports': [{u'votes': 0, u'group': u'Vialidad y Transito (SS)', u'created_at': u'2013-12-22T18:09:45-06:00', u'updated_at': u'2013-12-22T18:15:49-06:00', u'address_detail': {u'county': {u'long_name': u'Monterrey', u'short_name': u'Monterrey'}, u'neighborhood': {u'long_name': u'Contry Tesoro', u'short_name': u'Contry Tesoro'}, u'state': {u'long_name': u'Nuevo Le\xf3n', u'short_name': u'NL'}, u'formatted_address': u'Avenida Alfonso Reyes, Contry Tesoro, 64850 Monterrey, NL, M\xe9xico', u'zipcode': u'64850'}, u'content': u'*ACCIDENTE* En Alfonso Reyes y Las Musas. MTY #mtyfollow 17:59 via @custodesmty', u'state': u'closed', u'stars': 0.0, u'lat': u'25.64334232435947', u'is_public': True, u'ticket': u'#8DVO', u'lng': u'-100.27700725360774', u'categories': [u'ACCIDENTE']}, {u'votes': 0, u'group': u'Vialidad y Transito (SS)', u'created_at': u'2013-12-22T18:04:38-06:00', u'updated_at': u'2013-12-22T18:23:09-06:00', u'address_detail': {u'county': {u'long_name': u'Monterrey', u'short_name': u'Monterrey'}, u'neighborhood': {u'long_name': u'Centro', u'short_name': u'Centro'}, u'state': {u'long_name': u'Nuevo Le\xf3n', u'short_name': u'NL'}, u'formatted_address': u'Allende-Santiago, Villa de Santiago, NL, M\xe9xico', u'zipcode': u'64000'}, u'content': u'*ACCIDENTE* En Carr Nacional Allende altura de la entrada a San Antonino. ALL-12.22@17:52', u'state': u'closed', u'stars': 0.0, u'lat': u'25.3111465042625', u'is_public': True, u'ticket': u'#8DVN', u'lng': u'-100.04316288395785', u'categories': [u'ACCIDENTE']}, ...]}

But also you can ``limit`` the number of results, filter for categories or dates.

.. code-block:: pycon

    >>> from pycic.report import Report
    >>> from datetime import datetime
    >>> now = datetime.now()
    >>>
    >>> r = Report()
    >>> r.get(until=now, limit=5, for_category=407)
    {u'reports': [{u'votes': 0, u'group': u'Vialidad y Transito (SS)', u'created_at': u'2013-12-21T16:54:48-06:00', u'updated_at': u'2013-12-21T16:55:58-06:00', u'address_detail': {u'county': {u'long_name': u'Escobedo', u'short_name': u'Escobedo'}, u'neighborhood': {u'long_name': u'Hacienda del Canad\xe1', u'short_name': u'Hacienda del Canad\xe1'}, u'state': {u'long_name': u'Nuevo Le\xf3n', u'short_name': u'NL'}, u'formatted_address': u'Avenida Benito Ju\xe1rez 101, Hacienda del Canad\xe1, 66054 Escobedo, NL, M\xe9xico', u'zipcode': u'66054'}, u'content': u'*ACCIDENTE* En Av. Juarez una cuadra antes de Carr Colombia, ambos sentidos afectados. ESC #mtyfollow 16:52 via @drreynosa', u'state': u'closed', u'stars': 0.0, u'lat': u'25.78169151071929', u'is_public': True, u'ticket': u'#8DTM', u'lng': u'-100.29198115691543', u'categories': [u'ACCIDENTE']},...]}


If you want to create a new report, it's easy, the only required attributes are ``content`` and ``category``, but you are free to insert ``title``, ``first_name``, ``last_name``, ``return_path``, ``lat``, ``lng`` and ``video_url``.

.. code-block:: pycon

    >>> from pycic.report import Report
    >>> r = Report()
    >>> r.save(title="API Demo", content="API Demo", category="ACCIDENTE")
    {u'reports': {u'votes': 0, u'group': u'', u'created_at': u'2013-12-22T23:27:07-06:00', u'updated_at': u'2013-12-22T23:27:07-06:00', u'address_detail': {u'county': {u'long_name': None, u'short_name': None}, u'neighborhood': {u'long_name': None, u'short_name': None}, u'state': {u'long_name': None, u'short_name': None}, u'formatted_address': u'Monterrey, Nuevo Leon, Mexico', u'zipcode': None}, u'content': u'API Demo', u'state': u'received', u'stars': 0.0, u'lat': u'25.68442453605345', u'is_public': False, u'ticket': u'#8DW0', u'lng': u'-100.31773996210785', u'categories': []}}


Groups
++++++

You can get all the available groups

.. code-block:: pycon

    >>> from pycic.report import Group
    >>> g = Group()
    >>> g.get()
    {u'groups': [{u'id': 402, u'categories': [[u'FALTA ELECTRICIDAD', 423]], u'name': u'CFE Golfo Norte'}, {u'id': 396, u'categories': [[u'FUGA', 414], [u'RECOLECCION DE BASURA', 1572], [u'BACHE O VIA DA\xd1ADA', 412], [u'SEMAFORO DESCOMPUESTO', 411], [u'ALUMBRADO PUBLICO', 416], [u'ALCANTARILLAS', 1573], [u'PARQUES DESCUIDADOS', 421], [u'FALTA ELECTRICIDAD', 423]], u'name': u'CIAC APO'}, {u'id': 400, u'categories': [[u'FUGA', 414], [u'ALCANTARILLAS', 1573], [u'ALUMBRADO PUBLICO', 416], [u'FALTA ELECTRICIDAD', 423], [u'RECOLECCION DE BASURA', 1572], [u'PARQUES DESCUIDADOS', 421], [u'SEMAFORO DESCOMPUESTO', 411], [u'BACHE O VIA DA\xd1ADA', 412]], u'name': u'CIAC CAD'}, {u'id': 398, u'categories': [[u'FUGA', 414], [u'BACHE O VIA DA\xd1ADA', 412], [u'PARQUES DESCUIDADOS', 421], [u'SEMAFORO DESCOMPUESTO', 411], [u'ALCANTARILLAS', 1573], [u'FALTA ELECTRICIDAD', 423], [u'RECOLECCION DE BASURA', 1572], [u'ALUMBRADO PUBLICO', 416]], u'name': u'CIAC ESC'}, {u'id': 397, u'categories': [[u'FUGA', 414], [u'ALCANTARILLAS', 1573], [u'ALUMBRADO PUBLICO', 416], [u'FALTA ELECTRICIDAD', 423], [u'RECOLECCION DE BASURA', 1572], [u'PARQUES DESCUIDADOS', 421], [u'BACHE O VIA DA\xd1ADA', 412], [u'SEMAFORO DESCOMPUESTO', 411]], u'name': u'CIAC GAR'}, {u'id': 393, u'categories': [[u'FUGA', 414], [u'RECOLECCION DE BASURA', 1572], [u'ALUMBRADO PUBLICO', 416], [u'BACHE O VIA DA\xd1ADA', 412], [u'ALCANTARILLAS', 1573], [u'SEMAFORO DESCOMPUESTO', 411], [u'PARQUES DESCUIDADOS', 421], [u'FALTA ELECTRICIDAD', 423]], u'name': u'CIAC GPE'}, {u'id': 399, u'categories': [[u'FUGA', 414], [u'ALUMBRADO PUBLICO', 416], [u'ALCANTARILLAS', 1573], [u'RECOLECCION DE BASURA', 1572], [u'PARQUES DESCUIDADOS', 421], [u'FALTA ELECTRICIDAD', 423], [u'SEMAFORO DESCOMPUESTO', 411], [u'BACHE O VIA DA\xd1ADA', 412]], u'name': u'CIAC JUA'}, {u'id': 392, u'categories': [[u'SEMAFORO DESCOMPUESTO', 411], [u'BACHE O VIA DA\xd1ADA', 412], [u'ALUMBRADO PUBLICO', 416], [u'RECOLECCION DE BASURA', 1572], [u'FUGA', 414], [u'ALCANTARILLAS', 1573], [u'FALTA ELECTRICIDAD', 423], [u'PARQUES DESCUIDADOS', 421]], u'name': u'CIAC MTY'}, {u'id': 395, u'categories': [[u'FUGA', 414], [u'ALCANTARILLAS', 1573], [u'ALUMBRADO PUBLICO', 416], [u'FALTA ELECTRICIDAD', 423], [u'PARQUES DESCUIDADOS', 421], [u'RECOLECCION DE BASURA', 1572], [u'BACHE O VIA DA\xd1ADA', 412], [u'SEMAFORO DESCOMPUESTO', 411]], u'name': u'CIAC SC'}, {u'id': 394, u'categories': [[u'FUGA', 414], [u'ALCANTARILLAS', 1573], [u'ALUMBRADO PUBLICO', 416], [u'RECOLECCION DE BASURA', 1572], [u'PARQUES DESCUIDADOS', 421], [u'BACHE O VIA DA\xd1ADA', 412], [u'SEMAFORO DESCOMPUESTO', 411], [u'FALTA ELECTRICIDAD', 423]], u'name': u'CIAC SN'}, {u'id': 391, u'categories': [[u'FUGA', 414], [u'ALUMBRADO PUBLICO', 416], [u'FALTA ELECTRICIDAD', 423], [u'PARQUES DESCUIDADOS', 421], [u'RECOLECCION DE BASURA', 1572], [u'ALCANTARILLAS', 1573], [u'SEMAFORO DESCOMPUESTO', 411], [u'BACHE O VIA DA\xd1ADA', 412]], u'name': u'CIAC SP'}, {u'id': 401, u'categories': [[u'FUGA', 414], [u'ALCANTARILLAS', 1573], [u'ALUMBRADO PUBLICO', 416], [u'FALTA ELECTRICIDAD', 423], [u'RECOLECCION DE BASURA', 1572], [u'PARQUES DESCUIDADOS', 421], [u'SEMAFORO DESCOMPUESTO', 411], [u'BACHE O VIA DA\xd1ADA', 412]], u'name': u'CIAC STG'}, {u'id': 133, u'categories': [[u'AVISOS', 420], [u'EVENTO PUBLICO', 415], [u'OBSERVADOR CIUDADANO', 1578], [u'MTYMUYBIEN', 1614]], u'name': u'Comunidad'}, {u'id': 136, u'categories': [[u'EMERGENCIAS', 409]], u'name': u'Emergencias'}, {u'id': 257, u'categories': [[u'PROPUESTA VIALIDAD', 1103], [u'PROPUESTA COMUNIDAD', 1101], [u'PROPUESTA SEGURIDAD', 1102], [u'PROPUESTA SERV PUBLICOS', 1104]], u'name': u'Propuestas Ciudadanas (CS)'}, {u'id': 404, u'categories': [[u'FUGA', 414], [u'ALCANTARILLAS', 1573]], u'name': u'SADM Mty'}, {u'id': 403, u'categories': [[u'ROBO', 410], [u'SITUACION DE RIESGO', 418], [u'PERCEPCION DE INSEGURIDAD', 1613], [u'SECUESTRO', 422], [u'EXTORSION', 461], [u'HOMICIDIO', 1574], [u'SOSPECHOSO', 419], [u'AUTO ABANDONADO', 417], [u'DETENCION DE BANDAS', 1575], [u'INCENDIO', 408]], u'name': u'SEG MTY'}, {u'id': 135, u'categories': [[u'SOSPECHOSO', 419], [u'ROBO', 410], [u'SITUACION DE RIESGO', 418], [u'INCENDIO', 408], [u'SECUESTRO', 422], [u'AUTO ABANDONADO', 417], [u'EXTORSION', 461], [u'HOMICIDIO', 1574], [u'DETENCION DE BANDAS', 1575], [u'PERCEPCION DE INSEGURIDAD', 1613]], u'name': u'Seguridad'}, {u'id': 137, u'categories': [[u'FUGA', 414], [u'FALTA ELECTRICIDAD', 423], [u'ALUMBRADO PUBLICO', 416], [u'PARQUES DESCUIDADOS', 421], [u'RECOLECCION DE BASURA', 1572], [u'ALCANTARILLAS', 1573], [u'SEMAFORO DESCOMPUESTO', 411], [u'BACHE O VIA DA\xd1ADA', 412]], u'name': u'Servicios Publicos (CS)'}, {u'id': 134, u'categories': [[u'ACCIDENTE', 407], [u'VIALIDAD', 494], [u'OBRAS Y/O VIA CERRADA', 413]], u'name': u'Vialidad y Transito (SS)'}]}


Categories
++++++++++

You can get all the available categories

.. code-block:: pycon

    >>> from pycic.report import Category
    >>> c = Category()
    >>> c.get()
    {u'categories': [{u'group': [u'Vialidad y Transito (SS)'], u'metadata': False, u'type': u'blackbox', u'id': 407, u'name': u'ACCIDENTE'}, {u'group': [u'Servicios Publicos (CS)', u'CIAC SP', u'CIAC MTY', u'CIAC GPE', u'CIAC SN', u'CIAC SC', u'CIAC APO', u'CIAC GAR', u'CIAC ESC', u'CIAC JUA', u'CIAC STG', u'CIAC CAD', u'SADM Mty'], u'metadata': False, u'type': u'blackbox', u'id': 1573, u'name': u'ALCANTARILLAS'}, {u'group': [u'Servicios Publicos (CS)', u'CIAC SP', u'CIAC MTY', u'CIAC GPE', u'CIAC SN', u'CIAC SC', u'CIAC APO', u'CIAC GAR', u'CIAC ESC', u'CIAC JUA', u'CIAC STG', u'CIAC CAD'], u'metadata': False, u'type': u'blackbox', u'id': 416, u'name': u'ALUMBRADO PUBLICO'}, {u'group': [u'Seguridad', u'SEG MTY'], u'metadata': False, u'type': u'blackbox', u'id': 417, u'name': u'AUTO ABANDONADO'}, {u'group': [u'Comunidad'], u'metadata': False, u'type': u'blackbox', u'id': 420, u'name': u'AVISOS'}, {u'group': [u'Servicios Publicos (CS)', u'CIAC SP', u'CIAC MTY', u'CIAC GPE', u'CIAC SN', u'CIAC SC', u'CIAC APO', u'CIAC GAR', u'CIAC ESC', u'CIAC JUA', u'CIAC STG', u'CIAC CAD'], u'metadata': False, u'type': u'blackbox', u'id': 412, u'name': u'BACHE O VIA DA\xd1ADA'}, {u'group': [u'Seguridad', u'SEG MTY'], u'metadata': False, u'type': u'blackbox', u'id': 1575, u'name': u'DETENCION DE BANDAS'}, {u'group': [u'Emergencias'], u'metadata': False, u'type': u'blackbox', u'id': 409, u'name': u'EMERGENCIAS'}, {u'group': [u'Comunidad'], u'metadata': False, u'type': u'blackbox', u'id': 415, u'name': u'EVENTO PUBLICO'}, {u'group': [u'Seguridad', u'SEG MTY'], u'metadata': False, u'type': u'blackbox', u'id': 461, u'name': u'EXTORSION'}, {u'group': [u'Servicios Publicos (CS)', u'CIAC SP', u'CIAC MTY', u'CIAC GPE', u'CIAC SN', u'CIAC SC', u'CIAC APO', u'CIAC GAR', u'CIAC ESC', u'CIAC JUA', u'CIAC STG', u'CIAC CAD', u'CFE Golfo Norte'], u'metadata': False, u'type': u'blackbox', u'id': 423, u'name': u'FALTA ELECTRICIDAD'}, {u'group': [u'Servicios Publicos (CS)', u'CIAC SP', u'CIAC MTY', u'CIAC GPE', u'CIAC SN', u'CIAC SC', u'CIAC APO', u'CIAC GAR', u'CIAC ESC', u'CIAC JUA', u'CIAC STG', u'CIAC CAD', u'SADM Mty'], u'metadata': False, u'type': u'blackbox', u'id': 414, u'name': u'FUGA'}, {u'group': [u'Seguridad', u'SEG MTY'], u'metadata': False, u'type': u'blackbox', u'id': 1574, u'name': u'HOMICIDIO'}, {u'group': [u'Seguridad', u'SEG MTY'], u'metadata': False, u'type': u'blackbox', u'id': 408, u'name': u'INCENDIO'}, {u'group': [u'Comunidad'], u'metadata': False, u'type': u'blackbox', u'id': 1614, u'name': u'MTYMUYBIEN'}, {u'group': [u'Vialidad y Transito (SS)'], u'metadata': False, u'type': u'blackbox', u'id': 413, u'name': u'OBRAS Y/O VIA CERRADA'}, {u'group': [u'Comunidad'], u'metadata': False, u'type': u'blackbox', u'id': 1578, u'name': u'OBSERVADOR CIUDADANO'}, {u'group': [], u'metadata': False, u'type': u'blackbox', u'id': 424, u'name': u'OTROS'}, {u'group': [u'Servicios Publicos (CS)', u'CIAC SP', u'CIAC MTY', u'CIAC GPE', u'CIAC SN', u'CIAC SC', u'CIAC APO', u'CIAC GAR', u'CIAC ESC', u'CIAC JUA', u'CIAC STG', u'CIAC CAD'], u'metadata': False, u'type': u'blackbox', u'id': 421, u'name': u'PARQUES DESCUIDADOS'}, {u'group': [u'Seguridad', u'SEG MTY'], u'metadata': False, u'type': u'blackbox', u'id': 1613, u'name': u'PERCEPCION DE INSEGURIDAD'}, {u'group': [u'Propuestas Ciudadanas (CS)'], u'metadata': False, u'type': u'blackbox', u'id': 1101, u'name': u'PROPUESTA COMUNIDAD'}, {u'group': [u'Propuestas Ciudadanas (CS)'], u'metadata': False, u'type': u'blackbox', u'id': 1102, u'name': u'PROPUESTA SEGURIDAD'}, {u'group': [u'Propuestas Ciudadanas (CS)'], u'metadata': False, u'type': u'blackbox', u'id': 1104, u'name': u'PROPUESTA SERV PUBLICOS'}, {u'group': [u'Propuestas Ciudadanas (CS)'], u'metadata': False, u'type': u'blackbox', u'id': 1103, u'name': u'PROPUESTA VIALIDAD'}, {u'group': [u'Servicios Publicos (CS)', u'CIAC SP', u'CIAC MTY', u'CIAC GPE', u'CIAC SN', u'CIAC SC', u'CIAC APO', u'CIAC GAR', u'CIAC ESC', u'CIAC JUA', u'CIAC STG', u'CIAC CAD'], u'metadata': False, u'type': u'blackbox', u'id': 1572, u'name': u'RECOLECCION DE BASURA'}, {u'group': [u'Seguridad', u'SEG MTY'], u'metadata': False, u'type': u'blackbox', u'id': 410, u'name': u'ROBO'}, {u'group': [u'Seguridad', u'SEG MTY'], u'metadata': False, u'type': u'blackbox', u'id': 422, u'name': u'SECUESTRO'}, {u'group': [u'Servicios Publicos (CS)', u'CIAC SP', u'CIAC MTY', u'CIAC GPE', u'CIAC SN', u'CIAC SC', u'CIAC APO', u'CIAC GAR', u'CIAC ESC', u'CIAC JUA', u'CIAC STG', u'CIAC CAD'], u'metadata': False, u'type': u'blackbox', u'id': 411, u'name': u'SEMAFORO DESCOMPUESTO'}, {u'group': [u'Seguridad', u'SEG MTY'], u'metadata': False, u'type': u'blackbox', u'id': 418, u'name': u'SITUACION DE RIESGO'}, {u'group': [u'Seguridad', u'SEG MTY'], u'metadata': False, u'type': u'blackbox', u'id': 419, u'name': u'SOSPECHOSO'}, {u'group': [u'Vialidad y Transito (SS)'], u'metadata': False, u'type': u'blackbox', u'id': 494, u'name': u'VIALIDAD'}]}

Installation
++++++++++++

To install ``pycic`` you can use ``pip`` command:

.. code-block:: bash

    $ pip install pycic

Documentation
+++++++++++++

Documentation is available at http://pycic.readthedocs.org/en/latest/

Contribute
++++++++++

The repository_ is available on Github, if you want to contribute feel free and fork the repository to start making your changes and tests to the *master* branch.

.. _CIC: http://cic.mx/
.. _`Nuevo Leon`: http://nl.gob.mx/
.. _Saltillo: http://www.saltillo.gob.mx/
.. _repository: https://github.com/milmazz/pycic
