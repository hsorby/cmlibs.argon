OpenCMISS.Argon.ArgonDocument class Reference
=============================================

Manages and serializes argon file.

Public Member Functions
-----------------------

ArgonDocument(name='Argon') :ref:`ArgonDocument`

checkVersion(self, minimum_required)

deserialize(self, state)

findRegion(self, name)

freeVisualisationContents(self)

getMaterials(self)

getName(self)

getRootRegion(self)

getSpectrums(self)

getTessellations(self)

getViewManager(self)

getZincContext(self)

initialiseVisualisationContents(self)

serialize(self, basePath=None)


Detailed Description
--------------------

Manages and serializes argon file.

Member Function Documentation
-----------------------------

.. _ArgonDocument:

ArgonDocument(name='Argon')
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Initialize self.  See help(type(self)) for accurate signature.

checkVersion(self, minimum_required)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Check the version number of this Argon library. 


deserialize(self, state)
^^^^^^^^^^^^^^^^^^^^^^^^
    
**Parameters**

    *state:* string serialisation of Argon JSON document

findRegion(self, name)
^^^^^^^^^^^^^^^^^^^^^^
Returns the default region in the context. A convenience for applications that need only one region tree.


freeVisualisationContents(self)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Deletes subobjects of document to help free memory held by Zinc objects earlier.

getMaterials(self)
^^^^^^^^^^^^^^^^^^
Return the ArgonMaterial object which manages materials used to colour, texture and shade graphics. Note on startup only materials "default" and "default_selected" are defined, as white and red, respectively. Additional standard and custom materials can be defined using material module functions.

**Returns**
      The ArgonMaterial object, or NULL/invalid on failure.


getName(self)
^^^^^^^^^^^^^
Returns the name of the region.

Returns
On success: allocated string containing region name.

getRootRegion(self)
^^^^^^^^^^^^^^^^^^^
Returns the root region in the context. A convenience for applications that need only one region tree.

getSpectrums(self)
^^^^^^^^^^^^^^^^^^
Get the spectrum module which manages spectrum objects controlling how graphics data fields are converted into colours.

Returns
Handle to the spectrum module, or NULL/invalid handle on failure.

getTessellations(self)
^^^^^^^^^^^^^^^^^^^^^^
Get the tessellation module which manages objects controlling how curves are approximated by line segments in graphics.

Returns
Handle to the tesselation module, or NULL/invalid handle on failure.

getViewManager(self)
^^^^^^^^^^^^^^^^^^^^

getZincContext(self)
^^^^^^^^^^^^^^^^^^^^

initialiseVisualisationContents(self)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

serialize(self, basePath=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
