OpenCMISS.Argon.ArgonRegion class Reference
===========================================

Public Member Functions
-----------------------
ArgonRegion(name, zincRegion, parent=None)

addFieldTypeToDict(self, field, fieldType)

addModelSource(self, modelSource)

applyModelSource(self, modelSource)

clear(self)

connectRegionChange(self, callableObject)

createChild(self)

deserialize(self, dictInput)

freeContents(self)

getChild(self, index)

getChildCount(self)

getDisplayName(self)

getFieldTypeDict(self)

getModelSources(self)

getName(self)

getParent(self)

getPath(self)

getZincRegion(self)

remove(self)

removeChild(self, childRegion)

removeModelSource(self, modelSource)

replaceFieldTypeKey(self, oldName, newName)

serialize(self, basePath=None)

setName(self, name)

Detailed Description
--------------------


Member Function Documentation
-----------------------------

ArgonRegion(name, zincRegion, parent=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



addFieldTypeToDict(self, field, fieldType)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

addModelSource(self, modelSource)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Add model source, applying it if not currently editing

**Parameters**

    *modelSource:* The model source to add

applyModelSource(self, modelSource)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Apply model source, loading it or reloading it with all other sources as required

**Parameters**

    *modelSource:* The model source to apply

clear(self)
^^^^^^^^^^^
Clear all contents of region. Can be called for root region

connectRegionChange(self, callableObject)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Request callbacks on region tree changes.

**Parameters**
    *callableObject:* Callable object taking a NeonRegion argument and a boolean flag which is True if tree
    structure below region needs to be rebuilt.

createChild(self)
^^^^^^^^^^^^^^^^^
    Create a child region with a default name
    :return: The new Neon Region

deserialize(self, dictInput)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

freeContents(self)
^^^^^^^^^^^^^^^^^^
    Deletes subobjects of region to help free memory held by Zinc objects earlier.

getChild(self, index)
^^^^^^^^^^^^^^^^^^^^^

getChildCount(self)
^^^^^^^^^^^^^^^^^^^

getDisplayName(self)
^^^^^^^^^^^^^^^^^^^^

getFieldTypeDict(self)
^^^^^^^^^^^^^^^^^^^^^^

getModelSources(self)
^^^^^^^^^^^^^^^^^^^^^

getName(self)
^^^^^^^^^^^^^

getParent(self)
^^^^^^^^^^^^^^^

getPath(self)
^^^^^^^^^^^^^

getZincRegion(self)
^^^^^^^^^^^^^^^^^^^

remove(self)
^^^^^^^^^^^^
    Remove self from region tree and destroy; replace with blank region if root

removeChild(self, childRegion)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Remove child region and destroy

removeModelSource(self, modelSource)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Remove model source, reloading model if it removed source had been loaded
    :param modelSource: The model source to remove

replaceFieldTypeKey(self, oldName, newName)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

serialize(self, basePath=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

setName(self, name)
^^^^^^^^^^^^^^^^^^^