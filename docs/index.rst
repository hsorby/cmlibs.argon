CMLibs-Argon
============

The **CMLibs-Argon** is the core data structures for GUI applications using OpenCMISS-Zinc `opencmiss.org <http://opencmiss.org>`_.

Manages and serializes argon file.

Install
-------

Requirements
^^^^^^^^^^^^

python >= 3.6

opencmiss.zinc >= 3.6

pip install
^^^^^^^^^^^

CMLibs-Argon can be installed from PyPi.org with the following command::

  pip install cmlibs.argon

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

These modules are surfaced under the namespace package *cmlibs* within the *argon* package.
To use these modules the following import statement can be used::

  import cmlibs.argon.argondocument
  import cmlibs.argon.argonerror
  import cmlibs.argon.argonlogger
  import cmlibs.argon.argonmaterials
  import cmlibs.argon.argonmodelsources
  import cmlibs.argon.argonregion
  import cmlibs.argon.argonsceneviewer
  import cmlibs.argon.argonspectrums
  import cmlibs.argon.argontessellations
  import cmlibs.argon.argonviews

Classes
-------
.. .. automodule:: cmlibs.argon.argonsceneviewer
..    :members:

ArgonDocument Class
^^^^^^^^^^^^^^^^^^^

.. autoclass:: cmlibs.argon.argondocument.ArgonDocument
   :members:

ArgonError Class
^^^^^^^^^^^^^^^^

.. autoclass:: cmlibs.argon.argonerror.ArgonError
   :members:

ArgonLogger Class
^^^^^^^^^^^^^^^^^

.. autoclass:: cmlibs.argon.argonlogger.ArgonLogger
   :members:

ArgonMaterials Class
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: cmlibs.argon.argonmaterials.ArgonMaterials
   :members:

ArgonModelSourceFile Class
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: cmlibs.argon.argonmodelsources.ArgonModelSourceFile
   :members:

ArgonRegion Class
^^^^^^^^^^^^^^^^^

.. autoclass:: cmlibs.argon.argonregion.ArgonRegion
   :members:

ArgonSceneviewer Class
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: cmlibs.argon.argonsceneviewer.ArgonSceneviewer
   :members:

ArgonSpectrums Class
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: cmlibs.argon.argonspectrums.ArgonSpectrums
   :members:

ArgonTessellations Class
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: cmlibs.argon.argontessellations.ArgonTessellations
   :members:

ArgonView Class
^^^^^^^^^^^^^^^

.. autoclass:: cmlibs.argon.argonviews.ArgonView
   :members:

ArgonViewManager Class
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: cmlibs.argon.argonviews.ArgonViewManager
   :members:
