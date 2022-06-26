OpenCMISS.Argon.ArgonMaterials class Reference
==============================================

Public Member Functions
-----------------------
ArgonMaterials(zincContext)

Manages and serializes Zinc Materials.

deserialize(self, dictInput)

getZincContext(self)

serialize(self)


Detailed Description
--------------------
Manages and serializes argon file.

Member Function Documentation
-----------------------------

ArgonMaterials(zincContext)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Manages and serializes Zinc Materials.

deserialize(self, dict_input)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Read the json description to the argon Material object. This will change the spectrums in the spectrum module.

**Parameters**

*dict_input:* The string containing json description

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
