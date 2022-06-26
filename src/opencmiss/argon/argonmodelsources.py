"""
   Copyright 2015 University of Auckland

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
import os

from opencmiss.zinc.streamregion import StreaminformationRegion
from opencmiss.argon.argonerror import ArgonError


def _file_name_to_relative_path(file_name, base_path):
    if (base_path is None) or (not os.path.isabs(file_name)) or (os.path.commonprefix([file_name, base_path]) == ""):
        return file_name
    return os.path.relpath(file_name, base_path)


class ArgonModelSourceFile(object):

    def __init__(self, file_name=None, dict_input=None):
        self._time = None
        self._format = None
        self._edit = False
        self._region_name = None
        self._loaded = False
        if file_name is not None:
            self._file_name = file_name
        else:
            self._deserialize(dict_input)

    def getType(self):
        return "FILE"

    def addToZincStreaminformationRegion(self, stream_info):
        if self._edit:
            return
        if not self._file_name:
            self._edit = True
            return
        resource = stream_info.createStreamresourceFile(self._file_name)
        self._loaded = True
        if self._time is not None and self._time:
            time = self._time
            if not isinstance(self._time, float):
                time = float(self._time)
            stream_info.setResourceAttributeReal(resource, StreaminformationRegion.ATTRIBUTE_TIME, time)
        # if self._format is not None:
        #    if format == "EX":
        #        #can't set per-resource file format
        #        #streamInfo.setResourceFileFormat(resource, StreaminformationRegion.FILE_FORMAT_EX)

    def unloaded(self):
        self._loaded = False

    def getFileName(self):
        return self._file_name

    def setFileName(self, file_name):
        self._file_name = file_name

    def getRegionName(self):
        return self._region_name

    def setRegionName(self, region_name):
        self._region_name = region_name

    def getTime(self):
        return self._time

    def setTime(self, time):
        self._time = time

    def getDisplayName(self):
        editText = "[To Apply] " if self._edit else ""
        if self._time is None:
            timeText = ""
        else:
            timeText = ", time " + repr(self._time)
        displayFileName = os.path.basename(self._file_name)
        return editText + "File " + displayFileName + timeText

    def isLoaded(self):
        return self._loaded

    def isEdit(self):
        return self._edit

    def setEdit(self, edit):
        self._edit = edit

    def _deserialize(self, dict_input):
        # convert to absolute file path so can save Neon file to new location and get correct relative path
        self._file_name = os.path.abspath(dict_input["FileName"])
        if "Time" in dict_input:
            self._time = dict_input["Time"]
        if "Format" in dict_input:
            self._format = dict_input["Format"]
        if "Edit" in dict_input:
            self._edit = dict_input["Edit"]
        if "RegionName" in dict_input:
            self._region_name = dict_input["RegionName"]

    def serialize(self, base_path=None):
        dictOutput = {
            "Type": self.getType(),
            "FileName": _file_name_to_relative_path(self._file_name, base_path)
        }
        if self._region_name is not None:
            dictOutput["RegionName"] = self._region_name
        if self._time is not None:
            dictOutput["Time"] = self._time
        if self._edit:
            dictOutput["Edit"] = True
        return dictOutput


def deserializeArgonModelSource(dict_input):
    """
    Factory method for creating the appropriate neon model source type from the dict serialization
    """
    if "Type" not in dict_input:
        raise ArgonError("Model source is missing Type attribute")

    typeString = dict_input["Type"]
    if typeString == "FILE":
        modelSource = ArgonModelSourceFile(dict_input=dict_input)
    else:
        raise ArgonError("Model source has unrecognised Type " + typeString)
    return modelSource
