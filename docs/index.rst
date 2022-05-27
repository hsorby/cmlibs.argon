OpenCMISS-Argon
===============

The **OpenCMISS-Argon** is the core data structures for GUI applications using OpenCMISS-Zinc `opencmiss.org <http://opencmiss.org>`_.

Manages and serializes argon file.

.. note::

   This project is under active development.

Install
-------

Requirements
^^^^^^^^^^^^

python >= 3.6

opencmiss.zinc >= 3.6

pip install
^^^^^^^^^^^

OpenCMISS-Argon can be installed from PyPi.org with the following command::

  pip install opencmiss.argon

Usage
-----

These modules are surfaced under the namespace package *opencmiss* within the *argon* package.
To use these modules the following import statement can be used::

  import opencmiss.argon

Classes
-------

`ArgonDocument Class`_
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argondocument.ArgonDocument
   :members:

`ArgonRegion Class`_
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonregion.ArgonRegion
   :members:

`ArgonSpectrums Class`_
^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonspectrums.ArgonSpectrums
   :members:

`ArgonMaterials Class`_
^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonmaterials.ArgonMaterials
   :members:

`ArgonView Class`_
^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonviews.ArgonView
   :members:

`ArgonTessellations Class`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argontessellations.ArgonTessellations
   :members:

`ArgonError Class`_
^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonerror.ArgonError
   :members:

`ArgonLogger Class`_
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonlogger.ArgonLogger
   :members:

.. _ArgonDocument Class: classargondocument.rst
.. _ArgonRegion Class: classargonregion.rst
.. _ArgonSpectrums Class: classargonspectrums.rst
.. _ArgonMaterials Class: classargonmaterials.rst
.. _ArgonView Class: classargonview.rst
.. _ArgonTessellations Class: classargontessellations.rst
.. _ArgonError Class: classargonerror.rst
.. _ArgonLogger Class: classargonlogger.rst
