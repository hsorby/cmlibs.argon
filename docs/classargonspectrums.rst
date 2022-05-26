OpenCMISS.Argon.ArgonSpectrums class Reference
==============================================

Public Member Functions
-----------------------
ArgonSpectrums(zincContext)

deserialize(self, dictInput)

findOrCreateSpectrumGlyphColourBar(self, spectrum)

getZincContext(self)

removeSpectrumByName(self, name)

renameSpectrum(self, spectrum, name)

serialize(self)

Detailed Description
--------------------
Manages and serializes argon file.

Member Function Documentation
-----------------------------

ArgonSpectrums(zincContext)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Manages and serializes Zinc Spectrums within Argon.
Generates colour bar glyphs for spectrums, which is automatically done if if not found on loading.

deserialize(self, dictInput)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Read the json description to the argon spectrum object. This will change the spectrums in the spectrum module.

**Parameters**

*dictInput:* The string containing json description

findOrCreateSpectrumGlyphColourBar(self, spectrum)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Find or create a GlyphColourBar for spectrum in the glyph module.
Newly created colour bar is set up for display in the normalised window coordinates at left.

getZincContext(self)
^^^^^^^^^^^^^^^^^^^^
Return the zinc Context of current argon spectrum.

**Return**

The zinc Context of current argon spectrum.

removeSpectrumByName(self, name)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Unmanages spectrum and its colour bar. Note spectrum is only removed if neither are in use.

**Return**
True if spectrum and colour bar removed, false if failed i.e. either are in use.

renameSpectrum(self, spectrum, name)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Renames spectrum and its glyph
    
**Return** 
True on success, otherwise False (means name not set)

serialize(self)
^^^^^^^^^^^^^^^
Write the json file describing the spectrums in the argon spectrum object, which can be used to store the current spectrum settings.

**Returns**

Python json object containing the json description of argon spectrum object, otherwise 0;