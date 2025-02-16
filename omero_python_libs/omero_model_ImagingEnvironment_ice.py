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
# Generated from file `ImagingEnvironment.ice'
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

if 'Temperature' not in _M_omero.model.__dict__:
    _M_omero.model._t_Temperature = IcePy.declareClass('::omero::model::Temperature')
    _M_omero.model._t_TemperaturePrx = IcePy.declareProxy('::omero::model::Temperature')

if 'Pressure' not in _M_omero.model.__dict__:
    _M_omero.model._t_Pressure = IcePy.declareClass('::omero::model::Pressure')
    _M_omero.model._t_PressurePrx = IcePy.declareProxy('::omero::model::Pressure')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if 'ImagingEnvironment' not in _M_omero.model.__dict__:
    _M_omero.model.ImagingEnvironment = Ice.createTempClass()
    class ImagingEnvironment(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _temperature=None, _airPressure=None, _humidity=None, _co2percent=None, _map=None):
            if Ice.getType(self) == _M_omero.model.ImagingEnvironment:
                raise RuntimeError('omero.model.ImagingEnvironment is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._temperature = _temperature
            self._airPressure = _airPressure
            self._humidity = _humidity
            self._co2percent = _co2percent
            self._map = _map

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject', '::omero::model::ImagingEnvironment')

        def ice_id(self, current=None):
            return '::omero::model::ImagingEnvironment'

        def ice_staticId():
            return '::omero::model::ImagingEnvironment'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getTemperature(self, current=None):
            pass

        def setTemperature(self, theTemperature, current=None):
            pass

        def getAirPressure(self, current=None):
            pass

        def setAirPressure(self, theAirPressure, current=None):
            pass

        def getHumidity(self, current=None):
            pass

        def setHumidity(self, theHumidity, current=None):
            pass

        def getCo2percent(self, current=None):
            pass

        def setCo2percent(self, theCo2percent, current=None):
            pass

        def getMapAsMap(self, current=None):
            pass

        def getMap(self, current=None):
            pass

        def setMap(self, theMap, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_ImagingEnvironment)

        __repr__ = __str__

    _M_omero.model.ImagingEnvironmentPrx = Ice.createTempClass()
    class ImagingEnvironmentPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.ImagingEnvironment._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.ImagingEnvironment._op_setVersion.end(self, _r)

        def getTemperature(self, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getTemperature.invoke(self, ((), _ctx))

        def begin_getTemperature(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getTemperature.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getTemperature(self, _r):
            return _M_omero.model.ImagingEnvironment._op_getTemperature.end(self, _r)

        def setTemperature(self, theTemperature, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setTemperature.invoke(self, ((theTemperature, ), _ctx))

        def begin_setTemperature(self, theTemperature, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setTemperature.begin(self, ((theTemperature, ), _response, _ex, _sent, _ctx))

        def end_setTemperature(self, _r):
            return _M_omero.model.ImagingEnvironment._op_setTemperature.end(self, _r)

        def getAirPressure(self, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getAirPressure.invoke(self, ((), _ctx))

        def begin_getAirPressure(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getAirPressure.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getAirPressure(self, _r):
            return _M_omero.model.ImagingEnvironment._op_getAirPressure.end(self, _r)

        def setAirPressure(self, theAirPressure, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setAirPressure.invoke(self, ((theAirPressure, ), _ctx))

        def begin_setAirPressure(self, theAirPressure, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setAirPressure.begin(self, ((theAirPressure, ), _response, _ex, _sent, _ctx))

        def end_setAirPressure(self, _r):
            return _M_omero.model.ImagingEnvironment._op_setAirPressure.end(self, _r)

        def getHumidity(self, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getHumidity.invoke(self, ((), _ctx))

        def begin_getHumidity(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getHumidity.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getHumidity(self, _r):
            return _M_omero.model.ImagingEnvironment._op_getHumidity.end(self, _r)

        def setHumidity(self, theHumidity, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setHumidity.invoke(self, ((theHumidity, ), _ctx))

        def begin_setHumidity(self, theHumidity, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setHumidity.begin(self, ((theHumidity, ), _response, _ex, _sent, _ctx))

        def end_setHumidity(self, _r):
            return _M_omero.model.ImagingEnvironment._op_setHumidity.end(self, _r)

        def getCo2percent(self, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getCo2percent.invoke(self, ((), _ctx))

        def begin_getCo2percent(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getCo2percent.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getCo2percent(self, _r):
            return _M_omero.model.ImagingEnvironment._op_getCo2percent.end(self, _r)

        def setCo2percent(self, theCo2percent, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setCo2percent.invoke(self, ((theCo2percent, ), _ctx))

        def begin_setCo2percent(self, theCo2percent, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setCo2percent.begin(self, ((theCo2percent, ), _response, _ex, _sent, _ctx))

        def end_setCo2percent(self, _r):
            return _M_omero.model.ImagingEnvironment._op_setCo2percent.end(self, _r)

        def getMapAsMap(self, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getMapAsMap.invoke(self, ((), _ctx))

        def begin_getMapAsMap(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getMapAsMap.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getMapAsMap(self, _r):
            return _M_omero.model.ImagingEnvironment._op_getMapAsMap.end(self, _r)

        def getMap(self, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getMap.invoke(self, ((), _ctx))

        def begin_getMap(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_getMap.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getMap(self, _r):
            return _M_omero.model.ImagingEnvironment._op_getMap.end(self, _r)

        def setMap(self, theMap, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setMap.invoke(self, ((theMap, ), _ctx))

        def begin_setMap(self, theMap, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ImagingEnvironment._op_setMap.begin(self, ((theMap, ), _response, _ex, _sent, _ctx))

        def end_setMap(self, _r):
            return _M_omero.model.ImagingEnvironment._op_setMap.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.ImagingEnvironmentPrx.ice_checkedCast(proxy, '::omero::model::ImagingEnvironment', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.ImagingEnvironmentPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::ImagingEnvironment'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_ImagingEnvironmentPrx = IcePy.defineProxy('::omero::model::ImagingEnvironment', ImagingEnvironmentPrx)

    _M_omero.model._t_ImagingEnvironment = IcePy.declareClass('::omero::model::ImagingEnvironment')

    _M_omero.model._t_ImagingEnvironment = IcePy.defineClass('::omero::model::ImagingEnvironment', ImagingEnvironment, -1, (), True, False, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt, False, 0),
        ('_temperature', (), _M_omero.model._t_Temperature, False, 0),
        ('_airPressure', (), _M_omero.model._t_Pressure, False, 0),
        ('_humidity', (), _M_omero._t_RDouble, False, 0),
        ('_co2percent', (), _M_omero._t_RDouble, False, 0),
        ('_map', (), _M_omero.api._t_NamedValueList, False, 0)
    ))
    ImagingEnvironment._ice_type = _M_omero.model._t_ImagingEnvironment

    ImagingEnvironment._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RInt, False, 0), ())
    ImagingEnvironment._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RInt, False, 0),), (), None, ())
    ImagingEnvironment._op_getTemperature = IcePy.Operation('getTemperature', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Temperature, False, 0), ())
    ImagingEnvironment._op_setTemperature = IcePy.Operation('setTemperature', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Temperature, False, 0),), (), None, ())
    ImagingEnvironment._op_getAirPressure = IcePy.Operation('getAirPressure', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Pressure, False, 0), ())
    ImagingEnvironment._op_setAirPressure = IcePy.Operation('setAirPressure', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Pressure, False, 0),), (), None, ())
    ImagingEnvironment._op_getHumidity = IcePy.Operation('getHumidity', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    ImagingEnvironment._op_setHumidity = IcePy.Operation('setHumidity', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    ImagingEnvironment._op_getCo2percent = IcePy.Operation('getCo2percent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    ImagingEnvironment._op_setCo2percent = IcePy.Operation('setCo2percent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    ImagingEnvironment._op_getMapAsMap = IcePy.Operation('getMapAsMap', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.api._t_StringStringMap, False, 0), ())
    ImagingEnvironment._op_getMap = IcePy.Operation('getMap', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.api._t_NamedValueList, False, 0), ())
    ImagingEnvironment._op_setMap = IcePy.Operation('setMap', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.api._t_NamedValueList, False, 0),), (), None, ())

    _M_omero.model.ImagingEnvironment = ImagingEnvironment
    del ImagingEnvironment

    _M_omero.model.ImagingEnvironmentPrx = ImagingEnvironmentPrx
    del ImagingEnvironmentPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
