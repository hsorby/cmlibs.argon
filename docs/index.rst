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

pip install
^^^^^^^^^^^

OpenCMISS-Argon can be installed from PyPi.org with the following command::

  pip install opencmiss.argon

Usage
-----

OpenCMISS-Argon can be imported by following command::

  import opencmiss.argon


Project Structure
-----------------

Classes
-------

.. autoclass:: opencmiss.argon.argondocument.ArgonDocument
   :members:

`class ArgonDocument`_

`class ArgonRegion`_

`class ArgonSpectrums`_

`class ArgonMaterials`_

`class ArgonView`_

`class ArgonTessellations`_

`class ArgonError`_

`class ArgonLogger`_

.. _class ArgonDocument: classargondocument.rst
.. _class ArgonRegion: classargonregion.rst
.. _class ArgonSpectrums: classargonspectrums.rst
.. _class ArgonMaterials: classargonmaterials.rst
.. _class ArgonView: classargonview.rst
.. _class ArgonTessellations: classargontessellations.rst
.. _class ArgonError: classargonerror.rst
.. _class ArgonLogger: classargonlogger.rst
