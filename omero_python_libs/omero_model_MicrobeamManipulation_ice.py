# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.4
#
# <auto-generated>
#
# Generated from file `MicrobeamManipulation.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import omero_model_IObject_ice
import omero_RTypes_ice
import omero_model_RTypes_ice
import omero_System_ice
import omero_Collections_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Start of module omero
__name__ = 'omero'

# Start of module omero.model
__name__ = 'omero.model'

if 'MicrobeamManipulationType' not in _M_omero.model.__dict__:
    _M_omero.model._t_MicrobeamManipulationType = IcePy.declareClass('::omero::model::MicrobeamManipulationType')
    _M_omero.model._t_MicrobeamManipulationTypePrx = IcePy.declareProxy('::omero::model::MicrobeamManipulationType')

if 'LightSettings' not in _M_omero.model.__dict__:
    _M_omero.model._t_LightSettings = IcePy.declareClass('::omero::model::LightSettings')
    _M_omero.model._t_LightSettingsPrx = IcePy.declareProxy('::omero::model::LightSettings')

if 'Experiment' not in _M_omero.model.__dict__:
    _M_omero.model._t_Experiment = IcePy.declareClass('::omero::model::Experiment')
    _M_omero.model._t_ExperimentPrx = IcePy.declareProxy('::omero::model::Experiment')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if '_t_MicrobeamManipulationLightSourceSettingsSeq' not in _M_omero.model.__dict__:
    _M_omero.model._t_MicrobeamManipulationLightSourceSettingsSeq = IcePy.defineSequence('::omero::model::MicrobeamManipulationLightSourceSettingsSeq', (), _M_omero.model._t_LightSettings)

if 'MicrobeamManipulation' not in _M_omero.model.__dict__:
    _M_omero.model.MicrobeamManipulation = Ice.createTempClass()
    class MicrobeamManipulation(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _type=None, _lightSourceSettingsSeq=None, _lightSourceSettingsLoaded=False, _experiment=None, _description=None):
            if Ice.getType(self) == _M_omero.model.MicrobeamManipulation:
                raise RuntimeError('omero.model.MicrobeamManipulation is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._type = _type
            self._lightSourceSettingsSeq = _lightSourceSettingsSeq
            self._lightSourceSettingsLoaded = _lightSourceSettingsLoaded
            self._experiment = _experiment
            self._description = _description

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject', '::omero::model::MicrobeamManipulation')

        def ice_id(self, current=None):
            return '::omero::model::MicrobeamManipulation'

        def ice_staticId():
            return '::omero::model::MicrobeamManipulation'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getType(self, current=None):
            pass

        def setType(self, theType, current=None):
            pass

        def unloadLightSourceSettings(self, current=None):
            pass

        def sizeOfLightSourceSettings(self, current=None):
            pass

        def copyLightSourceSettings(self, current=None):
            pass

        def addLightSettings(self, target, current=None):
            pass

        def addAllLightSettingsSet(self, targets, current=None):
            pass

        def removeLightSettings(self, theTarget, current=None):
            pass

        def removeAllLightSettingsSet(self, targets, current=None):
            pass

        def clearLightSourceSettings(self, current=None):
            pass

        def reloadLightSourceSettings(self, toCopy, current=None):
            pass

        def getExperiment(self, current=None):
            pass

        def setExperiment(self, theExperiment, current=None):
            pass

        def getDescription(self, current=None):
            pass

        def setDescription(self, theDescription, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_MicrobeamManipulation)

        __repr__ = __str__

    _M_omero.model.MicrobeamManipulationPrx = Ice.createTempClass()
    class MicrobeamManipulationPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_setVersion.end(self, _r)

        def getType(self, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_getType.invoke(self, ((), _ctx))

        def begin_getType(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_getType.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getType(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_getType.end(self, _r)

        def setType(self, theType, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_setType.invoke(self, ((theType, ), _ctx))

        def begin_setType(self, theType, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_setType.begin(self, ((theType, ), _response, _ex, _sent, _ctx))

        def end_setType(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_setType.end(self, _r)

        def unloadLightSourceSettings(self, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_unloadLightSourceSettings.invoke(self, ((), _ctx))

        def begin_unloadLightSourceSettings(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_unloadLightSourceSettings.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_unloadLightSourceSettings(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_unloadLightSourceSettings.end(self, _r)

        def sizeOfLightSourceSettings(self, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_sizeOfLightSourceSettings.invoke(self, ((), _ctx))

        def begin_sizeOfLightSourceSettings(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_sizeOfLightSourceSettings.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_sizeOfLightSourceSettings(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_sizeOfLightSourceSettings.end(self, _r)

        def copyLightSourceSettings(self, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_copyLightSourceSettings.invoke(self, ((), _ctx))

        def begin_copyLightSourceSettings(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_copyLightSourceSettings.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_copyLightSourceSettings(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_copyLightSourceSettings.end(self, _r)

        def addLightSettings(self, target, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_addLightSettings.invoke(self, ((target, ), _ctx))

        def begin_addLightSettings(self, target, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_addLightSettings.begin(self, ((target, ), _response, _ex, _sent, _ctx))

        def end_addLightSettings(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_addLightSettings.end(self, _r)

        def addAllLightSettingsSet(self, targets, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_addAllLightSettingsSet.invoke(self, ((targets, ), _ctx))

        def begin_addAllLightSettingsSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_addAllLightSettingsSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_addAllLightSettingsSet(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_addAllLightSettingsSet.end(self, _r)

        def removeLightSettings(self, theTarget, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_removeLightSettings.invoke(self, ((theTarget, ), _ctx))

        def begin_removeLightSettings(self, theTarget, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_removeLightSettings.begin(self, ((theTarget, ), _response, _ex, _sent, _ctx))

        def end_removeLightSettings(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_removeLightSettings.end(self, _r)

        def removeAllLightSettingsSet(self, targets, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_removeAllLightSettingsSet.invoke(self, ((targets, ), _ctx))

        def begin_removeAllLightSettingsSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_removeAllLightSettingsSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_removeAllLightSettingsSet(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_removeAllLightSettingsSet.end(self, _r)

        def clearLightSourceSettings(self, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_clearLightSourceSettings.invoke(self, ((), _ctx))

        def begin_clearLightSourceSettings(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_clearLightSourceSettings.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_clearLightSourceSettings(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_clearLightSourceSettings.end(self, _r)

        def reloadLightSourceSettings(self, toCopy, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_reloadLightSourceSettings.invoke(self, ((toCopy, ), _ctx))

        def begin_reloadLightSourceSettings(self, toCopy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_reloadLightSourceSettings.begin(self, ((toCopy, ), _response, _ex, _sent, _ctx))

        def end_reloadLightSourceSettings(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_reloadLightSourceSettings.end(self, _r)

        def getExperiment(self, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_getExperiment.invoke(self, ((), _ctx))

        def begin_getExperiment(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_getExperiment.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getExperiment(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_getExperiment.end(self, _r)

        def setExperiment(self, theExperiment, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_setExperiment.invoke(self, ((theExperiment, ), _ctx))

        def begin_setExperiment(self, theExperiment, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_setExperiment.begin(self, ((theExperiment, ), _response, _ex, _sent, _ctx))

        def end_setExperiment(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_setExperiment.end(self, _r)

        def getDescription(self, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_getDescription.invoke(self, ((), _ctx))

        def begin_getDescription(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_getDescription.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDescription(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_getDescription.end(self, _r)

        def setDescription(self, theDescription, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_setDescription.invoke(self, ((theDescription, ), _ctx))

        def begin_setDescription(self, theDescription, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulation._op_setDescription.begin(self, ((theDescription, ), _response, _ex, _sent, _ctx))

        def end_setDescription(self, _r):
            return _M_omero.model.MicrobeamManipulation._op_setDescription.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.MicrobeamManipulationPrx.ice_checkedCast(proxy, '::omero::model::MicrobeamManipulation', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.MicrobeamManipulationPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::MicrobeamManipulation'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_MicrobeamManipulationPrx = IcePy.defineProxy('::omero::model::MicrobeamManipulation', MicrobeamManipulationPrx)

    _M_omero.model._t_MicrobeamManipulation = IcePy.declareClass('::omero::model::MicrobeamManipulation')

    _M_omero.model._t_MicrobeamManipulation = IcePy.defineClass('::omero::model::MicrobeamManipulation', MicrobeamManipulation, -1, (), True, False, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt, False, 0),
        ('_type', (), _M_omero.model._t_MicrobeamManipulationType, False, 0),
        ('_lightSourceSettingsSeq', (), _M_omero.model._t_MicrobeamManipulationLightSourceSettingsSeq, False, 0),
        ('_lightSourceSettingsLoaded', (), IcePy._t_bool, False, 0),
        ('_experiment', (), _M_omero.model._t_Experiment, False, 0),
        ('_description', (), _M_omero._t_RString, False, 0)
    ))
    MicrobeamManipulation._ice_type = _M_omero.model._t_MicrobeamManipulation

    MicrobeamManipulation._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RInt, False, 0), ())
    MicrobeamManipulation._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RInt, False, 0),), (), None, ())
    MicrobeamManipulation._op_getType = IcePy.Operation('getType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_MicrobeamManipulationType, False, 0), ())
    MicrobeamManipulation._op_setType = IcePy.Operation('setType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_MicrobeamManipulationType, False, 0),), (), None, ())
    MicrobeamManipulation._op_unloadLightSourceSettings = IcePy.Operation('unloadLightSourceSettings', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    MicrobeamManipulation._op_sizeOfLightSourceSettings = IcePy.Operation('sizeOfLightSourceSettings', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    MicrobeamManipulation._op_copyLightSourceSettings = IcePy.Operation('copyLightSourceSettings', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_MicrobeamManipulationLightSourceSettingsSeq, False, 0), ())
    MicrobeamManipulation._op_addLightSettings = IcePy.Operation('addLightSettings', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_LightSettings, False, 0),), (), None, ())
    MicrobeamManipulation._op_addAllLightSettingsSet = IcePy.Operation('addAllLightSettingsSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_MicrobeamManipulationLightSourceSettingsSeq, False, 0),), (), None, ())
    MicrobeamManipulation._op_removeLightSettings = IcePy.Operation('removeLightSettings', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_LightSettings, False, 0),), (), None, ())
    MicrobeamManipulation._op_removeAllLightSettingsSet = IcePy.Operation('removeAllLightSettingsSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_MicrobeamManipulationLightSourceSettingsSeq, False, 0),), (), None, ())
    MicrobeamManipulation._op_clearLightSourceSettings = IcePy.Operation('clearLightSourceSettings', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    MicrobeamManipulation._op_reloadLightSourceSettings = IcePy.Operation('reloadLightSourceSettings', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_MicrobeamManipulation, False, 0),), (), None, ())
    MicrobeamManipulation._op_getExperiment = IcePy.Operation('getExperiment', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Experiment, False, 0), ())
    MicrobeamManipulation._op_setExperiment = IcePy.Operation('setExperiment', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Experiment, False, 0),), (), None, ())
    MicrobeamManipulation._op_getDescription = IcePy.Operation('getDescription', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    MicrobeamManipulation._op_setDescription = IcePy.Operation('setDescription', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())

    _M_omero.model.MicrobeamManipulation = MicrobeamManipulation
    del MicrobeamManipulation

    _M_omero.model.MicrobeamManipulationPrx = MicrobeamManipulationPrx
    del MicrobeamManipulationPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
