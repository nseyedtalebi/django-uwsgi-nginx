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
# Generated from file `NumericAnnotation.ice'
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
import omero_model_BasicAnnotation_ice

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

if 'AnnotationAnnotationLink' not in _M_omero.model.__dict__:
    _M_omero.model._t_AnnotationAnnotationLink = IcePy.declareClass('::omero::model::AnnotationAnnotationLink')
    _M_omero.model._t_AnnotationAnnotationLinkPrx = IcePy.declareProxy('::omero::model::AnnotationAnnotationLink')

if 'Annotation' not in _M_omero.model.__dict__:
    _M_omero.model._t_Annotation = IcePy.declareClass('::omero::model::Annotation')
    _M_omero.model._t_AnnotationPrx = IcePy.declareProxy('::omero::model::Annotation')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if 'NumericAnnotation' not in _M_omero.model.__dict__:
    _M_omero.model.NumericAnnotation = Ice.createTempClass()
    class NumericAnnotation(_M_omero.model.BasicAnnotation):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _ns=None, _name=None, _description=None, _annotationLinksSeq=None, _annotationLinksLoaded=False, _annotationLinksCountPerOwner=None):
            if Ice.getType(self) == _M_omero.model.NumericAnnotation:
                raise RuntimeError('omero.model.NumericAnnotation is an abstract class')
            _M_omero.model.BasicAnnotation.__init__(self, _id, _details, _loaded, _version, _ns, _name, _description, _annotationLinksSeq, _annotationLinksLoaded, _annotationLinksCountPerOwner)

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Annotation', '::omero::model::BasicAnnotation', '::omero::model::IObject', '::omero::model::NumericAnnotation')

        def ice_id(self, current=None):
            return '::omero::model::NumericAnnotation'

        def ice_staticId():
            return '::omero::model::NumericAnnotation'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_NumericAnnotation)

        __repr__ = __str__

    _M_omero.model.NumericAnnotationPrx = Ice.createTempClass()
    class NumericAnnotationPrx(_M_omero.model.BasicAnnotationPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.NumericAnnotationPrx.ice_checkedCast(proxy, '::omero::model::NumericAnnotation', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.NumericAnnotationPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::NumericAnnotation'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_NumericAnnotationPrx = IcePy.defineProxy('::omero::model::NumericAnnotation', NumericAnnotationPrx)

    _M_omero.model._t_NumericAnnotation = IcePy.declareClass('::omero::model::NumericAnnotation')

    _M_omero.model._t_NumericAnnotation = IcePy.defineClass('::omero::model::NumericAnnotation', NumericAnnotation, -1, (), True, False, _M_omero.model._t_BasicAnnotation, (), ())
    NumericAnnotation._ice_type = _M_omero.model._t_NumericAnnotation

    _M_omero.model.NumericAnnotation = NumericAnnotation
    del NumericAnnotation

    _M_omero.model.NumericAnnotationPrx = NumericAnnotationPrx
    del NumericAnnotationPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
