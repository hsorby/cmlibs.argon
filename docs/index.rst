OpenCMISS-Argon
===============

The **OpenCMISS-Argon** is the core data structures for GUI applications using OpenCMISS-Zinc `opencmiss.org <http://opencmiss.org>`_.

Manages and serializes argon file.

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

This package provides ten modules

#. argondocument
#. argonerror
#. argonlogger
#. argonmaterials
#. argonmodelsources
#. argonregion
#. argonsceneviewer
#. argonspectrums
#. argontessellations
#. argonviews

These modules are surfaced under the namespace package *opencmiss* within the *argon* package.
To use these modules the following import statement can be used::

  import opencmiss.argon.argondocument
  import opencmiss.argon.argonerror
  import opencmiss.argon.argonlogger
  import opencmiss.argon.argonmaterials
  import opencmiss.argon.argonmodelsources
  import opencmiss.argon.argonregion
  import opencmiss.argon.argonsceneviewer
  import opencmiss.argon.argonspectrums
  import opencmiss.argon.argontessellations
  import opencmiss.argon.argonviews

Classes
-------
.. .. automodule:: opencmiss.argon.argonsceneviewer
..    :members:

ArgonDocument Class
^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argondocument.ArgonDocument
   :members:

ArgonError Class
^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonerror.ArgonError
   :members:

ArgonLogger Class
^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonlogger.ArgonLogger
   :members:

ArgonMaterials Class
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonmaterials.ArgonMaterials
   :members:

ArgonModelSourceFile Class
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonmodelsources.ArgonModelSourceFile
   :members:

ArgonRegion Class
^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonregion.ArgonRegion
   :members:

ArgonSceneviewer Class
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonsceneviewer.ArgonSceneviewer
   :members:

ArgonSpectrums Class
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonspectrums.ArgonSpectrums
   :members:

ArgonTessellations Class
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argontessellations.ArgonTessellations
   :members:

ArgonView Class
^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonviews.ArgonView
   :members:

ArgonViewManager Class
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: opencmiss.argon.argonviews.ArgonViewManager
   :members:
