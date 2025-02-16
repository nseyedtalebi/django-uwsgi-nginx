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
# Generated from file `Polyline.ice'
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
import omero_model_Shape_ice

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

if 'Roi' not in _M_omero.model.__dict__:
    _M_omero.model._t_Roi = IcePy.declareClass('::omero::model::Roi')
    _M_omero.model._t_RoiPrx = IcePy.declareProxy('::omero::model::Roi')

if 'AffineTransform' not in _M_omero.model.__dict__:
    _M_omero.model._t_AffineTransform = IcePy.declareClass('::omero::model::AffineTransform')
    _M_omero.model._t_AffineTransformPrx = IcePy.declareProxy('::omero::model::AffineTransform')

if 'Length' not in _M_omero.model.__dict__:
    _M_omero.model._t_Length = IcePy.declareClass('::omero::model::Length')
    _M_omero.model._t_LengthPrx = IcePy.declareProxy('::omero::model::Length')

if 'ShapeAnnotationLink' not in _M_omero.model.__dict__:
    _M_omero.model._t_ShapeAnnotationLink = IcePy.declareClass('::omero::model::ShapeAnnotationLink')
    _M_omero.model._t_ShapeAnnotationLinkPrx = IcePy.declareProxy('::omero::model::ShapeAnnotationLink')

if 'Annotation' not in _M_omero.model.__dict__:
    _M_omero.model._t_Annotation = IcePy.declareClass('::omero::model::Annotation')
    _M_omero.model._t_AnnotationPrx = IcePy.declareProxy('::omero::model::Annotation')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if 'Polyline' not in _M_omero.model.__dict__:
    _M_omero.model.Polyline = Ice.createTempClass()
    class Polyline(_M_omero.model.Shape):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _theZ=None, _theT=None, _theC=None, _roi=None, _locked=None, _transform=None, _fillColor=None, _fillRule=None, _strokeColor=None, _strokeDashArray=None, _strokeWidth=None, _fontFamily=None, _fontSize=None, _fontStyle=None, _annotationLinksSeq=None, _annotationLinksLoaded=False, _annotationLinksCountPerOwner=None, _points=None, _markerStart=None, _markerEnd=None, _textValue=None):
            if Ice.getType(self) == _M_omero.model.Polyline:
                raise RuntimeError('omero.model.Polyline is an abstract class')
            _M_omero.model.Shape.__init__(self, _id, _details, _loaded, _version, _theZ, _theT, _theC, _roi, _locked, _transform, _fillColor, _fillRule, _strokeColor, _strokeDashArray, _strokeWidth, _fontFamily, _fontSize, _fontStyle, _annotationLinksSeq, _annotationLinksLoaded, _annotationLinksCountPerOwner)
            self._points = _points
            self._markerStart = _markerStart
            self._markerEnd = _markerEnd
            self._textValue = _textValue

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject', '::omero::model::Polyline', '::omero::model::Shape')

        def ice_id(self, current=None):
            return '::omero::model::Polyline'

        def ice_staticId():
            return '::omero::model::Polyline'
        ice_staticId = staticmethod(ice_staticId)

        def getPoints(self, current=None):
            pass

        def setPoints(self, thePoints, current=None):
            pass

        def getMarkerStart(self, current=None):
            pass

        def setMarkerStart(self, theMarkerStart, current=None):
            pass

        def getMarkerEnd(self, current=None):
            pass

        def setMarkerEnd(self, theMarkerEnd, current=None):
            pass

        def getTextValue(self, current=None):
            pass

        def setTextValue(self, theTextValue, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Polyline)

        __repr__ = __str__

    _M_omero.model.PolylinePrx = Ice.createTempClass()
    class PolylinePrx(_M_omero.model.ShapePrx):

        def getPoints(self, _ctx=None):
            return _M_omero.model.Polyline._op_getPoints.invoke(self, ((), _ctx))

        def begin_getPoints(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Polyline._op_getPoints.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getPoints(self, _r):
            return _M_omero.model.Polyline._op_getPoints.end(self, _r)

        def setPoints(self, thePoints, _ctx=None):
            return _M_omero.model.Polyline._op_setPoints.invoke(self, ((thePoints, ), _ctx))

        def begin_setPoints(self, thePoints, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Polyline._op_setPoints.begin(self, ((thePoints, ), _response, _ex, _sent, _ctx))

        def end_setPoints(self, _r):
            return _M_omero.model.Polyline._op_setPoints.end(self, _r)

        def getMarkerStart(self, _ctx=None):
            return _M_omero.model.Polyline._op_getMarkerStart.invoke(self, ((), _ctx))

        def begin_getMarkerStart(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Polyline._op_getMarkerStart.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getMarkerStart(self, _r):
            return _M_omero.model.Polyline._op_getMarkerStart.end(self, _r)

        def setMarkerStart(self, theMarkerStart, _ctx=None):
            return _M_omero.model.Polyline._op_setMarkerStart.invoke(self, ((theMarkerStart, ), _ctx))

        def begin_setMarkerStart(self, theMarkerStart, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Polyline._op_setMarkerStart.begin(self, ((theMarkerStart, ), _response, _ex, _sent, _ctx))

        def end_setMarkerStart(self, _r):
            return _M_omero.model.Polyline._op_setMarkerStart.end(self, _r)

        def getMarkerEnd(self, _ctx=None):
            return _M_omero.model.Polyline._op_getMarkerEnd.invoke(self, ((), _ctx))

        def begin_getMarkerEnd(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Polyline._op_getMarkerEnd.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getMarkerEnd(self, _r):
            return _M_omero.model.Polyline._op_getMarkerEnd.end(self, _r)

        def setMarkerEnd(self, theMarkerEnd, _ctx=None):
            return _M_omero.model.Polyline._op_setMarkerEnd.invoke(self, ((theMarkerEnd, ), _ctx))

        def begin_setMarkerEnd(self, theMarkerEnd, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Polyline._op_setMarkerEnd.begin(self, ((theMarkerEnd, ), _response, _ex, _sent, _ctx))

        def end_setMarkerEnd(self, _r):
            return _M_omero.model.Polyline._op_setMarkerEnd.end(self, _r)

        def getTextValue(self, _ctx=None):
            return _M_omero.model.Polyline._op_getTextValue.invoke(self, ((), _ctx))

        def begin_getTextValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Polyline._op_getTextValue.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getTextValue(self, _r):
            return _M_omero.model.Polyline._op_getTextValue.end(self, _r)

        def setTextValue(self, theTextValue, _ctx=None):
            return _M_omero.model.Polyline._op_setTextValue.invoke(self, ((theTextValue, ), _ctx))

        def begin_setTextValue(self, theTextValue, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Polyline._op_setTextValue.begin(self, ((theTextValue, ), _response, _ex, _sent, _ctx))

        def end_setTextValue(self, _r):
            return _M_omero.model.Polyline._op_setTextValue.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.PolylinePrx.ice_checkedCast(proxy, '::omero::model::Polyline', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.PolylinePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::Polyline'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_PolylinePrx = IcePy.defineProxy('::omero::model::Polyline', PolylinePrx)

    _M_omero.model._t_Polyline = IcePy.declareClass('::omero::model::Polyline')

    _M_omero.model._t_Polyline = IcePy.defineClass('::omero::model::Polyline', Polyline, -1, (), True, False, _M_omero.model._t_Shape, (), (
        ('_points', (), _M_omero._t_RString, False, 0),
        ('_markerStart', (), _M_omero._t_RString, False, 0),
        ('_markerEnd', (), _M_omero._t_RString, False, 0),
        ('_textValue', (), _M_omero._t_RString, False, 0)
    ))
    Polyline._ice_type = _M_omero.model._t_Polyline

    Polyline._op_getPoints = IcePy.Operation('getPoints', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Polyline._op_setPoints = IcePy.Operation('setPoints', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    Polyline._op_getMarkerStart = IcePy.Operation('getMarkerStart', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Polyline._op_setMarkerStart = IcePy.Operation('setMarkerStart', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    Polyline._op_getMarkerEnd = IcePy.Operation('getMarkerEnd', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Polyline._op_setMarkerEnd = IcePy.Operation('setMarkerEnd', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    Polyline._op_getTextValue = IcePy.Operation('getTextValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Polyline._op_setTextValue = IcePy.Operation('setTextValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())

    _M_omero.model.Polyline = Polyline
    del Polyline

    _M_omero.model.PolylinePrx = PolylinePrx
    del PolylinePrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
