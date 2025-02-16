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
# Generated from file `Mask.ice'
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

if 'Pixels' not in _M_omero.model.__dict__:
    _M_omero.model._t_Pixels = IcePy.declareClass('::omero::model::Pixels')
    _M_omero.model._t_PixelsPrx = IcePy.declareProxy('::omero::model::Pixels')

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

if 'Mask' not in _M_omero.model.__dict__:
    _M_omero.model.Mask = Ice.createTempClass()
    class Mask(_M_omero.model.Shape):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _theZ=None, _theT=None, _theC=None, _roi=None, _locked=None, _transform=None, _fillColor=None, _fillRule=None, _strokeColor=None, _strokeDashArray=None, _strokeWidth=None, _fontFamily=None, _fontSize=None, _fontStyle=None, _annotationLinksSeq=None, _annotationLinksLoaded=False, _annotationLinksCountPerOwner=None, _x=None, _y=None, _width=None, _height=None, _pixels=None, _textValue=None, _bytes=None):
            if Ice.getType(self) == _M_omero.model.Mask:
                raise RuntimeError('omero.model.Mask is an abstract class')
            _M_omero.model.Shape.__init__(self, _id, _details, _loaded, _version, _theZ, _theT, _theC, _roi, _locked, _transform, _fillColor, _fillRule, _strokeColor, _strokeDashArray, _strokeWidth, _fontFamily, _fontSize, _fontStyle, _annotationLinksSeq, _annotationLinksLoaded, _annotationLinksCountPerOwner)
            self._x = _x
            self._y = _y
            self._width = _width
            self._height = _height
            self._pixels = _pixels
            self._textValue = _textValue
            self._bytes = _bytes

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject', '::omero::model::Mask', '::omero::model::Shape')

        def ice_id(self, current=None):
            return '::omero::model::Mask'

        def ice_staticId():
            return '::omero::model::Mask'
        ice_staticId = staticmethod(ice_staticId)

        def getX(self, current=None):
            pass

        def setX(self, theX, current=None):
            pass

        def getY(self, current=None):
            pass

        def setY(self, theY, current=None):
            pass

        def getWidth(self, current=None):
            pass

        def setWidth(self, theWidth, current=None):
            pass

        def getHeight(self, current=None):
            pass

        def setHeight(self, theHeight, current=None):
            pass

        def getPixels(self, current=None):
            pass

        def setPixels(self, thePixels, current=None):
            pass

        def getTextValue(self, current=None):
            pass

        def setTextValue(self, theTextValue, current=None):
            pass

        def getBytes(self, current=None):
            pass

        def setBytes(self, theBytes, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Mask)

        __repr__ = __str__

    _M_omero.model.MaskPrx = Ice.createTempClass()
    class MaskPrx(_M_omero.model.ShapePrx):

        def getX(self, _ctx=None):
            return _M_omero.model.Mask._op_getX.invoke(self, ((), _ctx))

        def begin_getX(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_getX.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getX(self, _r):
            return _M_omero.model.Mask._op_getX.end(self, _r)

        def setX(self, theX, _ctx=None):
            return _M_omero.model.Mask._op_setX.invoke(self, ((theX, ), _ctx))

        def begin_setX(self, theX, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_setX.begin(self, ((theX, ), _response, _ex, _sent, _ctx))

        def end_setX(self, _r):
            return _M_omero.model.Mask._op_setX.end(self, _r)

        def getY(self, _ctx=None):
            return _M_omero.model.Mask._op_getY.invoke(self, ((), _ctx))

        def begin_getY(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_getY.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getY(self, _r):
            return _M_omero.model.Mask._op_getY.end(self, _r)

        def setY(self, theY, _ctx=None):
            return _M_omero.model.Mask._op_setY.invoke(self, ((theY, ), _ctx))

        def begin_setY(self, theY, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_setY.begin(self, ((theY, ), _response, _ex, _sent, _ctx))

        def end_setY(self, _r):
            return _M_omero.model.Mask._op_setY.end(self, _r)

        def getWidth(self, _ctx=None):
            return _M_omero.model.Mask._op_getWidth.invoke(self, ((), _ctx))

        def begin_getWidth(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_getWidth.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getWidth(self, _r):
            return _M_omero.model.Mask._op_getWidth.end(self, _r)

        def setWidth(self, theWidth, _ctx=None):
            return _M_omero.model.Mask._op_setWidth.invoke(self, ((theWidth, ), _ctx))

        def begin_setWidth(self, theWidth, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_setWidth.begin(self, ((theWidth, ), _response, _ex, _sent, _ctx))

        def end_setWidth(self, _r):
            return _M_omero.model.Mask._op_setWidth.end(self, _r)

        def getHeight(self, _ctx=None):
            return _M_omero.model.Mask._op_getHeight.invoke(self, ((), _ctx))

        def begin_getHeight(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_getHeight.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getHeight(self, _r):
            return _M_omero.model.Mask._op_getHeight.end(self, _r)

        def setHeight(self, theHeight, _ctx=None):
            return _M_omero.model.Mask._op_setHeight.invoke(self, ((theHeight, ), _ctx))

        def begin_setHeight(self, theHeight, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_setHeight.begin(self, ((theHeight, ), _response, _ex, _sent, _ctx))

        def end_setHeight(self, _r):
            return _M_omero.model.Mask._op_setHeight.end(self, _r)

        def getPixels(self, _ctx=None):
            return _M_omero.model.Mask._op_getPixels.invoke(self, ((), _ctx))

        def begin_getPixels(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_getPixels.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getPixels(self, _r):
            return _M_omero.model.Mask._op_getPixels.end(self, _r)

        def setPixels(self, thePixels, _ctx=None):
            return _M_omero.model.Mask._op_setPixels.invoke(self, ((thePixels, ), _ctx))

        def begin_setPixels(self, thePixels, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_setPixels.begin(self, ((thePixels, ), _response, _ex, _sent, _ctx))

        def end_setPixels(self, _r):
            return _M_omero.model.Mask._op_setPixels.end(self, _r)

        def getTextValue(self, _ctx=None):
            return _M_omero.model.Mask._op_getTextValue.invoke(self, ((), _ctx))

        def begin_getTextValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_getTextValue.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getTextValue(self, _r):
            return _M_omero.model.Mask._op_getTextValue.end(self, _r)

        def setTextValue(self, theTextValue, _ctx=None):
            return _M_omero.model.Mask._op_setTextValue.invoke(self, ((theTextValue, ), _ctx))

        def begin_setTextValue(self, theTextValue, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_setTextValue.begin(self, ((theTextValue, ), _response, _ex, _sent, _ctx))

        def end_setTextValue(self, _r):
            return _M_omero.model.Mask._op_setTextValue.end(self, _r)

        def getBytes(self, _ctx=None):
            return _M_omero.model.Mask._op_getBytes.invoke(self, ((), _ctx))

        def begin_getBytes(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_getBytes.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getBytes(self, _r):
            return _M_omero.model.Mask._op_getBytes.end(self, _r)

        def setBytes(self, theBytes, _ctx=None):
            return _M_omero.model.Mask._op_setBytes.invoke(self, ((theBytes, ), _ctx))

        def begin_setBytes(self, theBytes, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Mask._op_setBytes.begin(self, ((theBytes, ), _response, _ex, _sent, _ctx))

        def end_setBytes(self, _r):
            return _M_omero.model.Mask._op_setBytes.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.MaskPrx.ice_checkedCast(proxy, '::omero::model::Mask', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.MaskPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::Mask'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_MaskPrx = IcePy.defineProxy('::omero::model::Mask', MaskPrx)

    _M_omero.model._t_Mask = IcePy.declareClass('::omero::model::Mask')

    _M_omero.model._t_Mask = IcePy.defineClass('::omero::model::Mask', Mask, -1, (), True, False, _M_omero.model._t_Shape, (), (
        ('_x', (), _M_omero._t_RDouble, False, 0),
        ('_y', (), _M_omero._t_RDouble, False, 0),
        ('_width', (), _M_omero._t_RDouble, False, 0),
        ('_height', (), _M_omero._t_RDouble, False, 0),
        ('_pixels', (), _M_omero.model._t_Pixels, False, 0),
        ('_textValue', (), _M_omero._t_RString, False, 0),
        ('_bytes', (), _M_Ice._t_ByteSeq, False, 0)
    ))
    Mask._ice_type = _M_omero.model._t_Mask

    Mask._op_getX = IcePy.Operation('getX', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Mask._op_setX = IcePy.Operation('setX', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Mask._op_getY = IcePy.Operation('getY', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Mask._op_setY = IcePy.Operation('setY', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Mask._op_getWidth = IcePy.Operation('getWidth', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Mask._op_setWidth = IcePy.Operation('setWidth', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Mask._op_getHeight = IcePy.Operation('getHeight', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Mask._op_setHeight = IcePy.Operation('setHeight', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Mask._op_getPixels = IcePy.Operation('getPixels', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Pixels, False, 0), ())
    Mask._op_setPixels = IcePy.Operation('setPixels', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Pixels, False, 0),), (), None, ())
    Mask._op_getTextValue = IcePy.Operation('getTextValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Mask._op_setTextValue = IcePy.Operation('setTextValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    Mask._op_getBytes = IcePy.Operation('getBytes', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Ice._t_ByteSeq, False, 0), ())
    Mask._op_setBytes = IcePy.Operation('setBytes', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Ice._t_ByteSeq, False, 0),), (), None, ())

    _M_omero.model.Mask = Mask
    del Mask

    _M_omero.model.MaskPrx = MaskPrx
    del MaskPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
