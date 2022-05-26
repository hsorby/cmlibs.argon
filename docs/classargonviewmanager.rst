OpenCMISS.Argon.ArgonViewManager class Reference
================================================

Public Member Functions
-----------------------
ArgonViewManager(zincContext)

Manages and serializes ArgonViews.

addView(self, view_type, name=None)

deserialize(self, d)

getActiveView(self)

getView(self, index)

getViews(self)

getZincContext(self)

removeView(self, identifier)

serialize(self)

setActiveView(self, view)

setViews(self, views)

updateSceneviewers(self, view_index, sceneviewers_info)


Detailed Description
--------------------
Manages and serializes argon file.

Member Function Documentation
-----------------------------

ArgonMaterials(zincContext)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Manages and serializes Zinc Materials.

deserialize(self, dictInput)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Read the json description to the argon Material object. This will change the spectrums in the spectrum module.

**Parameters**

*dictInput:* The string containing json description

getZincContext(self)
^^^^^^^^^^^^^^^^^^^^
Return the zinc Context of current argon spectrum.

**Return**

The zinc Context of current argon spectrum.

serialize(self)
^^^^^^^^^^^^^^^
Write the json file describing the Materials in the argon spectrum object, which can be used to store the current material settings.

**Returns**

Python json object containing the json description of argon Materials object, otherwise 0;