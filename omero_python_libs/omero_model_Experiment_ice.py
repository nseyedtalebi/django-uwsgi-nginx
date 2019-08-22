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
# Generated from file `Experiment.ice'
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

if 'ExperimentType' not in _M_omero.model.__dict__:
    _M_omero.model._t_ExperimentType = IcePy.declareClass('::omero::model::ExperimentType')
    _M_omero.model._t_ExperimentTypePrx = IcePy.declareProxy('::omero::model::ExperimentType')

if 'MicrobeamManipulation' not in _M_omero.model.__dict__:
    _M_omero.model._t_MicrobeamManipulation = IcePy.declareClass('::omero::model::MicrobeamManipulation')
    _M_omero.model._t_MicrobeamManipulationPrx = IcePy.declareProxy('::omero::model::MicrobeamManipulation')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if '_t_ExperimentMicrobeamManipulationSeq' not in _M_omero.model.__dict__:
    _M_omero.model._t_ExperimentMicrobeamManipulationSeq = IcePy.defineSequence('::omero::model::ExperimentMicrobeamManipulationSeq', (), _M_omero.model._t_MicrobeamManipulation)

if 'Experiment' not in _M_omero.model.__dict__:
    _M_omero.model.Experiment = Ice.createTempClass()
    class Experiment(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _type=None, _microbeamManipulationSeq=None, _microbeamManipulationLoaded=False, _description=None):
            if Ice.getType(self) == _M_omero.model.Experiment:
                raise RuntimeError('omero.model.Experiment is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._type = _type
            self._microbeamManipulationSeq = _microbeamManipulationSeq
            self._microbeamManipulationLoaded = _microbeamManipulationLoaded
            self._description = _description

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Experiment', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::Experiment'

        def ice_staticId():
            return '::omero::model::Experiment'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getType(self, current=None):
            pass

        def setType(self, theType, current=None):
            pass

        def unloadMicrobeamManipulation(self, current=None):
            pass

        def sizeOfMicrobeamManipulation(self, current=None):
            pass

        def copyMicrobeamManipulation(self, current=None):
            pass

        def addMicrobeamManipulation(self, target, current=None):
            pass

        def addAllMicrobeamManipulationSet(self, targets, current=None):
            pass

        def removeMicrobeamManipulation(self, theTarget, current=None):
            pass

        def removeAllMicrobeamManipulationSet(self, targets, current=None):
            pass

        def clearMicrobeamManipulation(self, current=None):
            pass

        def reloadMicrobeamManipulation(self, toCopy, current=None):
            pass

        def getDescription(self, current=None):
            pass

        def setDescription(self, theDescription, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Experiment)

        __repr__ = __str__

    _M_omero.model.ExperimentPrx = Ice.createTempClass()
    class ExperimentPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.Experiment._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.Experiment._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.Experiment._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.Experiment._op_setVersion.end(self, _r)

        def getType(self, _ctx=None):
            return _M_omero.model.Experiment._op_getType.invoke(self, ((), _ctx))

        def begin_getType(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_getType.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getType(self, _r):
            return _M_omero.model.Experiment._op_getType.end(self, _r)

        def setType(self, theType, _ctx=None):
            return _M_omero.model.Experiment._op_setType.invoke(self, ((theType, ), _ctx))

        def begin_setType(self, theType, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_setType.begin(self, ((theType, ), _response, _ex, _sent, _ctx))

        def end_setType(self, _r):
            return _M_omero.model.Experiment._op_setType.end(self, _r)

        def unloadMicrobeamManipulation(self, _ctx=None):
            return _M_omero.model.Experiment._op_unloadMicrobeamManipulation.invoke(self, ((), _ctx))

        def begin_unloadMicrobeamManipulation(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_unloadMicrobeamManipulation.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_unloadMicrobeamManipulation(self, _r):
            return _M_omero.model.Experiment._op_unloadMicrobeamManipulation.end(self, _r)

        def sizeOfMicrobeamManipulation(self, _ctx=None):
            return _M_omero.model.Experiment._op_sizeOfMicrobeamManipulation.invoke(self, ((), _ctx))

        def begin_sizeOfMicrobeamManipulation(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_sizeOfMicrobeamManipulation.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_sizeOfMicrobeamManipulation(self, _r):
            return _M_omero.model.Experiment._op_sizeOfMicrobeamManipulation.end(self, _r)

        def copyMicrobeamManipulation(self, _ctx=None):
            return _M_omero.model.Experiment._op_copyMicrobeamManipulation.invoke(self, ((), _ctx))

        def begin_copyMicrobeamManipulation(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_copyMicrobeamManipulation.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_copyMicrobeamManipulation(self, _r):
            return _M_omero.model.Experiment._op_copyMicrobeamManipulation.end(self, _r)

        def addMicrobeamManipulation(self, target, _ctx=None):
            return _M_omero.model.Experiment._op_addMicrobeamManipulation.invoke(self, ((target, ), _ctx))

        def begin_addMicrobeamManipulation(self, target, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_addMicrobeamManipulation.begin(self, ((target, ), _response, _ex, _sent, _ctx))

        def end_addMicrobeamManipulation(self, _r):
            return _M_omero.model.Experiment._op_addMicrobeamManipulation.end(self, _r)

        def addAllMicrobeamManipulationSet(self, targets, _ctx=None):
            return _M_omero.model.Experiment._op_addAllMicrobeamManipulationSet.invoke(self, ((targets, ), _ctx))

        def begin_addAllMicrobeamManipulationSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_addAllMicrobeamManipulationSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_addAllMicrobeamManipulationSet(self, _r):
            return _M_omero.model.Experiment._op_addAllMicrobeamManipulationSet.end(self, _r)

        def removeMicrobeamManipulation(self, theTarget, _ctx=None):
            return _M_omero.model.Experiment._op_removeMicrobeamManipulation.invoke(self, ((theTarget, ), _ctx))

        def begin_removeMicrobeamManipulation(self, theTarget, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_removeMicrobeamManipulation.begin(self, ((theTarget, ), _response, _ex, _sent, _ctx))

        def end_removeMicrobeamManipulation(self, _r):
            return _M_omero.model.Experiment._op_removeMicrobeamManipulation.end(self, _r)

        def removeAllMicrobeamManipulationSet(self, targets, _ctx=None):
            return _M_omero.model.Experiment._op_removeAllMicrobeamManipulationSet.invoke(self, ((targets, ), _ctx))

        def begin_removeAllMicrobeamManipulationSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_removeAllMicrobeamManipulationSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_removeAllMicrobeamManipulationSet(self, _r):
            return _M_omero.model.Experiment._op_removeAllMicrobeamManipulationSet.end(self, _r)

        def clearMicrobeamManipulation(self, _ctx=None):
            return _M_omero.model.Experiment._op_clearMicrobeamManipulation.invoke(self, ((), _ctx))

        def begin_clearMicrobeamManipulation(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_clearMicrobeamManipulation.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_clearMicrobeamManipulation(self, _r):
            return _M_omero.model.Experiment._op_clearMicrobeamManipulation.end(self, _r)

        def reloadMicrobeamManipulation(self, toCopy, _ctx=None):
            return _M_omero.model.Experiment._op_reloadMicrobeamManipulation.invoke(self, ((toCopy, ), _ctx))

        def begin_reloadMicrobeamManipulation(self, toCopy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_reloadMicrobeamManipulation.begin(self, ((toCopy, ), _response, _ex, _sent, _ctx))

        def end_reloadMicrobeamManipulation(self, _r):
            return _M_omero.model.Experiment._op_reloadMicrobeamManipulation.end(self, _r)

        def getDescription(self, _ctx=None):
            return _M_omero.model.Experiment._op_getDescription.invoke(self, ((), _ctx))

        def begin_getDescription(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_getDescription.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDescription(self, _r):
            return _M_omero.model.Experiment._op_getDescription.end(self, _r)

        def setDescription(self, theDescription, _ctx=None):
            return _M_omero.model.Experiment._op_setDescription.invoke(self, ((theDescription, ), _ctx))

        def begin_setDescription(self, theDescription, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Experiment._op_setDescription.begin(self, ((theDescription, ), _response, _ex, _sent, _ctx))

        def end_setDescription(self, _r):
            return _M_omero.model.Experiment._op_setDescription.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.ExperimentPrx.ice_checkedCast(proxy, '::omero::model::Experiment', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.ExperimentPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::Experiment'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_ExperimentPrx = IcePy.defineProxy('::omero::model::Experiment', ExperimentPrx)

    _M_omero.model._t_Experiment = IcePy.declareClass('::omero::model::Experiment')

    _M_omero.model._t_Experiment = IcePy.defineClass('::omero::model::Experiment', Experiment, -1, (), True, False, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt, False, 0),
        ('_type', (), _M_omero.model._t_ExperimentType, False, 0),
        ('_microbeamManipulationSeq', (), _M_omero.model._t_ExperimentMicrobeamManipulationSeq, False, 0),
        ('_microbeamManipulationLoaded', (), IcePy._t_bool, False, 0),
        ('_description', (), _M_omero._t_RString, False, 0)
    ))
    Experiment._ice_type = _M_omero.model._t_Experiment

    Experiment._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RInt, False, 0), ())
    Experiment._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RInt, False, 0),), (), None, ())
    Experiment._op_getType = IcePy.Operation('getType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_ExperimentType, False, 0), ())
    Experiment._op_setType = IcePy.Operation('setType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimentType, False, 0),), (), None, ())
    Experiment._op_unloadMicrobeamManipulation = IcePy.Operation('unloadMicrobeamManipulation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Experiment._op_sizeOfMicrobeamManipulation = IcePy.Operation('sizeOfMicrobeamManipulation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    Experiment._op_copyMicrobeamManipulation = IcePy.Operation('copyMicrobeamManipulation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_ExperimentMicrobeamManipulationSeq, False, 0), ())
    Experiment._op_addMicrobeamManipulation = IcePy.Operation('addMicrobeamManipulation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_MicrobeamManipulation, False, 0),), (), None, ())
    Experiment._op_addAllMicrobeamManipulationSet = IcePy.Operation('addAllMicrobeamManipulationSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimentMicrobeamManipulationSeq, False, 0),), (), None, ())
    Experiment._op_removeMicrobeamManipulation = IcePy.Operation('removeMicrobeamManipulation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_MicrobeamManipulation, False, 0),), (), None, ())
    Experiment._op_removeAllMicrobeamManipulationSet = IcePy.Operation('removeAllMicrobeamManipulationSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimentMicrobeamManipulationSeq, False, 0),), (), None, ())
    Experiment._op_clearMicrobeamManipulation = IcePy.Operation('clearMicrobeamManipulation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Experiment._op_reloadMicrobeamManipulation = IcePy.Operation('reloadMicrobeamManipulation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Experiment, False, 0),), (), None, ())
    Experiment._op_getDescription = IcePy.Operation('getDescription', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Experiment._op_setDescription = IcePy.Operation('setDescription', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())

    _M_omero.model.Experiment = Experiment
    del Experiment

    _M_omero.model.ExperimentPrx = ExperimentPrx
    del ExperimentPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
