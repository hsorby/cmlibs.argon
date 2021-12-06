"""
   Copyright 2016 University of Auckland

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import json

from opencmiss.zinc.status import OK as ZINC_OK
from opencmiss.argon.argonerror import ArgonError
from opencmiss.argon.argonsceneviewer import ArgonSceneviewer


class ArgonViews(object):
    """
    Manages and serializes Zinc Materials.
    """

    def __init__(self, zincContext):
        self._zincContext = zincContext
        self._views = None
        self._activeView = None
        self._sceneviewer = None
        self._sceneviewers = []
        
    def getZincContext(self):
        return self._zincContext

    def deserialize(self, d):
        # d = json.loads(s)
        self._activeView = d["ActiveView"] if "ActiveView" in d else None
        self._views = d["Views"] if "Views" in d else None
        
    def serialize(self):
        dictOutput = {}
        if self._name:
            dictOutput["ActiveView"] = self._name
        dictOutput["Views"] = {}
        if self._sceneviewers:
            tmpOutput = []
            for sceneviewer in self._sceneviewers:
                tmpOutput.append(sceneviewer.serialize())
            dictOutput["Views"] = tmpOutput
        if not dictOutput["Model"]:
            dictOutput.pop("Model")
        if self._zincRegion:
            fieldmodule = self._zincRegion.getFieldmodule()
            fieldmoduleDescription = fieldmodule.writeDescription()
            dictOutput["Fieldmodule"] = json.loads(fieldmoduleDescription)

            scene = self._zincRegion.getScene()
            sceneDescription = scene.writeDescription()
            dictOutput["Scene"] = json.loads(sceneDescription)
        if self._children:
            tmpOutput = []
            for child in self._children:
                tmpOutput.append(child.serialize(basePath))
            dictOutput["ChildRegions"] = tmpOutput
        return dictOutput
