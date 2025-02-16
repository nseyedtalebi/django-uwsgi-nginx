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
# Generated from file `RTypes.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import omero_model_IObject_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Start of module omero
__name__ = 'omero'

if 'RObject' not in _M_omero.__dict__:
    _M_omero.RObject = Ice.createTempClass()
    class RObject(_M_omero.RType):
        """
        Wrapper for an omero.model.IObject instance.
        """
        def __init__(self, _val=None):
            if Ice.getType(self) == _M_omero.RObject:
                raise RuntimeError('omero.RObject is an abstract class')
            _M_omero.RType.__init__(self)
            self._val = _val

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::RObject', '::omero::RType')

        def ice_id(self, current=None):
            return '::omero::RObject'

        def ice_staticId():
            return '::omero::RObject'
        ice_staticId = staticmethod(ice_staticId)

        def getValue(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero._t_RObject)

        __repr__ = __str__

    _M_omero.RObjectPrx = Ice.createTempClass()
    class RObjectPrx(_M_omero.RTypePrx):

        def getValue(self, _ctx=None):
            return _M_omero.RObject._op_getValue.invoke(self, ((), _ctx))

        def begin_getValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.RObject._op_getValue.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getValue(self, _r):
            return _M_omero.RObject._op_getValue.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.RObjectPrx.ice_checkedCast(proxy, '::omero::RObject', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.RObjectPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::RObject'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero._t_RObjectPrx = IcePy.defineProxy('::omero::RObject', RObjectPrx)

    _M_omero._t_RObject = IcePy.declareClass('::omero::RObject')

    _M_omero._t_RObject = IcePy.defineClass('::omero::RObject', RObject, -1, (), True, False, _M_omero._t_RType, (), (('_val', (), _M_omero.model._t_IObject, False, 0),))
    RObject._ice_type = _M_omero._t_RObject

    RObject._op_getValue = IcePy.Operation('getValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_IObject, False, 0), ())

    _M_omero.RObject = RObject
    del RObject

    _M_omero.RObjectPrx = RObjectPrx
    del RObjectPrx

# End of module omero
