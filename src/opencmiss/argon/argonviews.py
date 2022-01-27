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
    Manages and serializes ArgonViews.
    """

    def __init__(self, zincContext):
        self._zincContext = zincContext
        self._views = []
        self._activeView = None

    def getZincContext(self):
        return self._zincContext

    def deserialize(self, d):
        self._activeView = d["ActiveView"] if "ActiveView" in d else None
        if  "Views" in d:
            for i in d["Views"]:
                view = ArgonView(self._zincContext)
                view.deserialize(i)
                self._views.append(view)
        
    def serialize(self):
        dictOutput = {}
        if self._activeView:
            dictOutput["ActiveView"] = self._activeView
        dictOutput["Views"] = []
        if self._views:
            tmpOutput = []
            for view in self._views:
                tmpOutput.append(view.serialize())
            dictOutput["Views"] = tmpOutput
        return dictOutput

    def getActiveView(self):
        return self._activeView

    def getViews(self):
        return self._views

    def updateSceneviewers(self, sceneviewerwidget_list):
        for sceneviewerwidget in sceneviewerwidget_list:
            for view in self._views:
                sceneviewer = sceneviewerwidget.getSceneviewer()
                region = sceneviewer.getScene().getRegion().getName()
                view.updateSceneviewer(region, sceneviewer)

class ArgonView(object):
    """
    Manages and serializes Single View.
    """

    def __init__(self, zincContext):
        self._zincContext = zincContext
        self._name = None
        self._gridSpecification = None
        self._scenes = []

    def getZincContext(self):
        return self._zincContext

    def deserialize(self, d):
        self._name = d["Name"] if "Name" in d else None
        self._gridSpecification = d["GridSpecification"] if "GridSpecification" in d else None
        if "Scenes" in d:
            for s in d["Scenes"]:
                if "Sceneviewer" in s:
                    sceneviewer = ArgonSceneviewer(self._zincContext)
                    s["Sceneviewer"]["Scene"] = s["Path"]
                    sceneviewer.deserialize(s["Sceneviewer"])
                    s["Sceneviewer"] = sceneviewer
                self._scenes.append(s)
        
    def serialize(self):
        dictOutput = {}
        if self._name:
            dictOutput["Name"] = self._name
        if self._gridSpecification:
            dictOutput["GridSpecification"] = self._gridSpecification
        dictOutput["Scenes"] = []
        if self._scenes:
            for scene in self._scenes:
                tmpOutput = scene
                tmpOutput["Sceneviewer"] = scene["Sceneviewer"].serialize()
                print("serialize", scene["Path"], scene["Sceneviewer"]["EyePosition"])
                dictOutput["Scenes"].append(tmpOutput)
        return dictOutput

    def getName(self):
        return self._name

    def getScenes(self):
        return self._scenes

    def updateSceneviewer(self, rigon, sceneviewer):
        for scene in self._scenes:
            print("Update", scene["Path"], rigon)
            if scene["Path"] == rigon:
                scene["Sceneviewer"].updateParameters(sceneviewer)
                print("Update", scene["Path"], scene["Sceneviewer"]._eye_position)