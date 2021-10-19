##################################################################
# base  - Copyright ANSYS. All Rights Reserved.
# ##################################################################
# CREATION:      2021.08.17
# VERSION:       1.0.0
#
# OVERVIEW
# ========
# This script is generated for showing scripting capabilities purpose.
# It contains the base class (parent class) for all other classes and provides access to SCDM low-level API functions
# and methods.
#
# ##################################################################
# https://opensource.org/licenses/MIT
#
# Copyright 2021 Ansys, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The user agrees to this disclaimer and user agreement with the download or usage
# of the provided files.
#
# ##################################################################

# Python Script, API Version = V20 Beta

import clr
import os
import re
clr.AddReference('System.Collections')
from System.Collections.Generic import List
from System.Drawing import Color


class VersionError(KeyError):
    """
    Used to raise API version error
    """


class BaseSCDM(object):
    def __init__(self, SpaceClaim, supported_versions=None):
        """
        Base class that contains all common used objects. This class serves more as an abstract class.
        Optionally performs validation that API used by user is supported.
        Args:
            SpaceClaim: SpaceClaim object
            supported_versions (list/tuple): list of supported API versions
        """
        api = getattr(SpaceClaim, "Api")
        for obj in dir(api):
            try:
                api_version = re.match(r"V(\d+)$", obj).group(0)
                if supported_versions:
                    if api_version not in supported_versions:
                        msg = "SpaceClaim API {} is not supported. ".format(api_version)
                        msg += "Please use one of the following {}".format(", ".join(supported_versions))
                        raise VersionError(msg)

                scdm_api = getattr(api, api_version)
                break
            except AttributeError:
                continue
        else:
            raise AttributeError("No Api version found under SpaceClaim object")

        self.Color = Color
        self.List = List
        self.scdm_api = scdm_api

        self.BodySelection = scdm_api.Scripting.Selection.BodySelection
        self.CloseDocument = scdm_api.Scripting.Helpers.DocumentHelper.CloseDocument
        self.ColorHelper = scdm_api.Scripting.Helpers.ColorHelper
        self.ComponentExtensions = scdm_api.Scripting.Extensions.ComponentExtensions
        self.Copy = scdm_api.Scripting.Commands.Copy
        self.CreateNewDocument = scdm_api.Scripting.Helpers.DocumentHelper.CreateNewDocument
        self.Delete = scdm_api.Scripting.Commands.Delete
        self.DesignBodyExtensions = scdm_api.Scripting.Extensions.DesignBodyExtensions
        self.DocumentSave = scdm_api.Scripting.Commands.DocumentSave
        self.FixDuplicateFaces = scdm_api.Scripting.Commands.FixDuplicateFaces
        self.GetActiveDocument = scdm_api.Scripting.Helpers.DocumentHelper.GetActiveDocument
        self.GetOriginal = scdm_api.Scripting.Extensions.DocObjectExtensions.GetOriginal
        self.GetRootPart = scdm_api.Scripting.Helpers.DocumentHelper.GetRootPart
        self.IComponent = scdm_api.IComponent
        self.ICoordinateAxis = scdm_api.ICoordinateAxis
        self.ICoordinateSystem = scdm_api.ICoordinateSystem
        self.IDesignBody = scdm_api.IDesignBody
        self.IDesignCurve = scdm_api.IDesignCurve
        self.IPart = scdm_api.IPart
        self.Layers = scdm_api.Scripting.Commands.Layers
        self.NamedSelection = scdm_api.Scripting.Commands.NamedSelection
        self.Paste = scdm_api.Scripting.Commands.Paste
        self.PartExtensions = scdm_api.Scripting.Extensions.PartExtensions
        self.Selection = scdm_api.Scripting.Selection.Selection
        self.StitchFaces = scdm_api.Scripting.Commands.StitchFaces

def get_scdm_install_location(version):
    """
    Function to get installation path of SpaceClaim
    Args:
        version (int): version in format <XXX> eg 211

    Returns: path of SCDM installation
    """

    ansys_install_dir = os.environ["AWP_ROOT{}".format(version)]
    scdm_install_dir = os.path.join(ansys_install_dir, "scdm")
    return scdm_install_dir
