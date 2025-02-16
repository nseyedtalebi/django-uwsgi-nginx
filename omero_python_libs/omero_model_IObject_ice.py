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
# Generated from file `IObject.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import omero_RTypes_ice
import omero_ModelF_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Start of module omero
__name__ = 'omero'

# Start of module omero.model
__name__ = 'omero.model'

if 'IObject' not in _M_omero.model.__dict__:
    _M_omero.model.IObject = Ice.createTempClass()
    class IObject(Ice.Object):
        """
        Base class of all model types. On the
        server, the interface ome.model.IObject
        unifies the model. In Ice, interfaces have
        a more remote connotation.
        Members:
        id -- The database id for this entity. Of RLong value
        so that transient entities can have a null id.
        details -- Internal details (permissions, owner, etc.) for
        this entity. All entities have Details, and even
        a newly created object will have a non-null
        Details instance. (In the OMERO provided mapping!)
        loaded -- An unloaded object contains no state other than id. An
        exception will be raised if any field other than id is
        accessed via the OMERO-generated methods. Unloaded objects
        are useful as pointers or proxies to server-side state.
        """
        def __init__(self, _id=None, _details=None, _loaded=False):
            if Ice.getType(self) == _M_omero.model.IObject:
                raise RuntimeError('omero.model.IObject is an abstract class')
            self._id = _id
            self._details = _details
            self._loaded = _loaded

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::IObject'

        def ice_staticId():
            return '::omero::model::IObject'
        ice_staticId = staticmethod(ice_staticId)

        def getId(self, current=None):
            pass

        def setId(self, id, current=None):
            pass

        def getDetails(self, current=None):
            pass

        def proxy(self, current=None):
            """
            Return another instance of the same type as this instance
            constructed as if by: new InstanceI( this.id.val, false );
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def shallowCopy(self, current=None):
            """
            Return another instance of the same type as this instance
            with all single-value entities unloaded and all members of
            collections also unloaded.
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def unload(self, current=None):
            """
            Sets the loaded boolean to false and empties all state
            from this entity to make sending it over the network
            less costly.
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def unloadCollections(self, current=None):
            """
            Each collection can also be unloaded, independently
            of the object itself. To unload all collections, use:
            object.unloadCollections();
            This is useful when it is possible that a collection no
            longer represents the state in the database, and passing the
            collections back to the server might delete some entities.
            Sending back empty collections can also save a significant
            amount of bandwidth, when working with large data graphs.
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def unloadDetails(self, current=None):
            """
            As with collections, the objects under details can link
            to many other objects. Unloading the details can same
            bandwidth and simplify the server logic.
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def isLoaded(self, current=None):
            """
            Tests if the objects are loaded or not. If this value is false, then
            any method call on this instance other than getId
            or setId will result in an exception.
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def isGlobal(self, current=None):
            """
            Marker interface which means that special rules apply
            for both reading and writing these instances.
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def isLink(self, current=None):
            """
            A link between two other types.
            Methods provided:
            - getParent()
            - getChild()
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def isMutable(self, current=None):
            """
            The server will persist changes made to these types.
            Methods provided:
            - getVersion()
            - setVersion()
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def isAnnotated(self, current=None):
            """
            Allows for the attachment of any omero.model.Annotation
            subclasses. Methods provided are:
            - linkAnnotation(Annotation)
            -
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_IObject)

        __repr__ = __str__

    _M_omero.model.IObjectPrx = Ice.createTempClass()
    class IObjectPrx(Ice.ObjectPrx):

        def getId(self, _ctx=None):
            return _M_omero.model.IObject._op_getId.invoke(self, ((), _ctx))

        def begin_getId(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_getId.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getId(self, _r):
            return _M_omero.model.IObject._op_getId.end(self, _r)

        def setId(self, id, _ctx=None):
            return _M_omero.model.IObject._op_setId.invoke(self, ((id, ), _ctx))

        def begin_setId(self, id, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_setId.begin(self, ((id, ), _response, _ex, _sent, _ctx))

        def end_setId(self, _r):
            return _M_omero.model.IObject._op_setId.end(self, _r)

        def getDetails(self, _ctx=None):
            return _M_omero.model.IObject._op_getDetails.invoke(self, ((), _ctx))

        def begin_getDetails(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_getDetails.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDetails(self, _r):
            return _M_omero.model.IObject._op_getDetails.end(self, _r)

        """
        Return another instance of the same type as this instance
        constructed as if by: new InstanceI( this.id.val, false );
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def proxy(self, _ctx=None):
            return _M_omero.model.IObject._op_proxy.invoke(self, ((), _ctx))

        """
        Return another instance of the same type as this instance
        constructed as if by: new InstanceI( this.id.val, false );
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_proxy(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_proxy.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Return another instance of the same type as this instance
        constructed as if by: new InstanceI( this.id.val, false );
        Arguments:
        """
        def end_proxy(self, _r):
            return _M_omero.model.IObject._op_proxy.end(self, _r)

        """
        Return another instance of the same type as this instance
        with all single-value entities unloaded and all members of
        collections also unloaded.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def shallowCopy(self, _ctx=None):
            return _M_omero.model.IObject._op_shallowCopy.invoke(self, ((), _ctx))

        """
        Return another instance of the same type as this instance
        with all single-value entities unloaded and all members of
        collections also unloaded.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_shallowCopy(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_shallowCopy.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Return another instance of the same type as this instance
        with all single-value entities unloaded and all members of
        collections also unloaded.
        Arguments:
        """
        def end_shallowCopy(self, _r):
            return _M_omero.model.IObject._op_shallowCopy.end(self, _r)

        """
        Sets the loaded boolean to false and empties all state
        from this entity to make sending it over the network
        less costly.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def unload(self, _ctx=None):
            return _M_omero.model.IObject._op_unload.invoke(self, ((), _ctx))

        """
        Sets the loaded boolean to false and empties all state
        from this entity to make sending it over the network
        less costly.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_unload(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_unload.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Sets the loaded boolean to false and empties all state
        from this entity to make sending it over the network
        less costly.
        Arguments:
        """
        def end_unload(self, _r):
            return _M_omero.model.IObject._op_unload.end(self, _r)

        """
        Each collection can also be unloaded, independently
        of the object itself. To unload all collections, use:
        object.unloadCollections();
        This is useful when it is possible that a collection no
        longer represents the state in the database, and passing the
        collections back to the server might delete some entities.
        Sending back empty collections can also save a significant
        amount of bandwidth, when working with large data graphs.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def unloadCollections(self, _ctx=None):
            return _M_omero.model.IObject._op_unloadCollections.invoke(self, ((), _ctx))

        """
        Each collection can also be unloaded, independently
        of the object itself. To unload all collections, use:
        object.unloadCollections();
        This is useful when it is possible that a collection no
        longer represents the state in the database, and passing the
        collections back to the server might delete some entities.
        Sending back empty collections can also save a significant
        amount of bandwidth, when working with large data graphs.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_unloadCollections(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_unloadCollections.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Each collection can also be unloaded, independently
        of the object itself. To unload all collections, use:
        object.unloadCollections();
        This is useful when it is possible that a collection no
        longer represents the state in the database, and passing the
        collections back to the server might delete some entities.
        Sending back empty collections can also save a significant
        amount of bandwidth, when working with large data graphs.
        Arguments:
        """
        def end_unloadCollections(self, _r):
            return _M_omero.model.IObject._op_unloadCollections.end(self, _r)

        """
        As with collections, the objects under details can link
        to many other objects. Unloading the details can same
        bandwidth and simplify the server logic.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def unloadDetails(self, _ctx=None):
            return _M_omero.model.IObject._op_unloadDetails.invoke(self, ((), _ctx))

        """
        As with collections, the objects under details can link
        to many other objects. Unloading the details can same
        bandwidth and simplify the server logic.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_unloadDetails(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_unloadDetails.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        As with collections, the objects under details can link
        to many other objects. Unloading the details can same
        bandwidth and simplify the server logic.
        Arguments:
        """
        def end_unloadDetails(self, _r):
            return _M_omero.model.IObject._op_unloadDetails.end(self, _r)

        """
        Tests if the objects are loaded or not. If this value is false, then
        any method call on this instance other than getId
        or setId will result in an exception.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def isLoaded(self, _ctx=None):
            return _M_omero.model.IObject._op_isLoaded.invoke(self, ((), _ctx))

        """
        Tests if the objects are loaded or not. If this value is false, then
        any method call on this instance other than getId
        or setId will result in an exception.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_isLoaded(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_isLoaded.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Tests if the objects are loaded or not. If this value is false, then
        any method call on this instance other than getId
        or setId will result in an exception.
        Arguments:
        """
        def end_isLoaded(self, _r):
            return _M_omero.model.IObject._op_isLoaded.end(self, _r)

        """
        Marker interface which means that special rules apply
        for both reading and writing these instances.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def isGlobal(self, _ctx=None):
            return _M_omero.model.IObject._op_isGlobal.invoke(self, ((), _ctx))

        """
        Marker interface which means that special rules apply
        for both reading and writing these instances.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_isGlobal(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_isGlobal.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Marker interface which means that special rules apply
        for both reading and writing these instances.
        Arguments:
        """
        def end_isGlobal(self, _r):
            return _M_omero.model.IObject._op_isGlobal.end(self, _r)

        """
        A link between two other types.
        Methods provided:
        - getParent()
        - getChild()
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def isLink(self, _ctx=None):
            return _M_omero.model.IObject._op_isLink.invoke(self, ((), _ctx))

        """
        A link between two other types.
        Methods provided:
        - getParent()
        - getChild()
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_isLink(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_isLink.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        A link between two other types.
        Methods provided:
        - getParent()
        - getChild()
        Arguments:
        """
        def end_isLink(self, _r):
            return _M_omero.model.IObject._op_isLink.end(self, _r)

        """
        The server will persist changes made to these types.
        Methods provided:
        - getVersion()
        - setVersion()
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def isMutable(self, _ctx=None):
            return _M_omero.model.IObject._op_isMutable.invoke(self, ((), _ctx))

        """
        The server will persist changes made to these types.
        Methods provided:
        - getVersion()
        - setVersion()
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_isMutable(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_isMutable.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        The server will persist changes made to these types.
        Methods provided:
        - getVersion()
        - setVersion()
        Arguments:
        """
        def end_isMutable(self, _r):
            return _M_omero.model.IObject._op_isMutable.end(self, _r)

        """
        Allows for the attachment of any omero.model.Annotation
        subclasses. Methods provided are:
        - linkAnnotation(Annotation)
        -
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def isAnnotated(self, _ctx=None):
            return _M_omero.model.IObject._op_isAnnotated.invoke(self, ((), _ctx))

        """
        Allows for the attachment of any omero.model.Annotation
        subclasses. Methods provided are:
        - linkAnnotation(Annotation)
        -
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_isAnnotated(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.IObject._op_isAnnotated.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Allows for the attachment of any omero.model.Annotation
        subclasses. Methods provided are:
        - linkAnnotation(Annotation)
        -
        Arguments:
        """
        def end_isAnnotated(self, _r):
            return _M_omero.model.IObject._op_isAnnotated.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.IObjectPrx.ice_checkedCast(proxy, '::omero::model::IObject', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.IObjectPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::IObject'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_IObjectPrx = IcePy.defineProxy('::omero::model::IObject', IObjectPrx)

    _M_omero.model._t_IObject = IcePy.declareClass('::omero::model::IObject')

    _M_omero.model._t_IObject = IcePy.defineClass('::omero::model::IObject', IObject, -1, (), True, False, None, (), (
        ('_id', (), _M_omero._t_RLong, False, 0),
        ('_details', (), _M_omero.model._t_Details, False, 0),
        ('_loaded', (), IcePy._t_bool, False, 0)
    ))
    IObject._ice_type = _M_omero.model._t_IObject

    IObject._op_getId = IcePy.Operation('getId', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RLong, False, 0), ())
    IObject._op_setId = IcePy.Operation('setId', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RLong, False, 0),), (), None, ())
    IObject._op_getDetails = IcePy.Operation('getDetails', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Details, False, 0), ())
    IObject._op_proxy = IcePy.Operation('proxy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_IObject, False, 0), ())
    IObject._op_shallowCopy = IcePy.Operation('shallowCopy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_IObject, False, 0), ())
    IObject._op_unload = IcePy.Operation('unload', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    IObject._op_unloadCollections = IcePy.Operation('unloadCollections', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    IObject._op_unloadDetails = IcePy.Operation('unloadDetails', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    IObject._op_isLoaded = IcePy.Operation('isLoaded', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_bool, False, 0), ())
    IObject._op_isGlobal = IcePy.Operation('isGlobal', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_bool, False, 0), ())
    IObject._op_isLink = IcePy.Operation('isLink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_bool, False, 0), ())
    IObject._op_isMutable = IcePy.Operation('isMutable', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_bool, False, 0), ())
    IObject._op_isAnnotated = IcePy.Operation('isAnnotated', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_bool, False, 0), ())

    _M_omero.model.IObject = IObject
    del IObject

    _M_omero.model.IObjectPrx = IObjectPrx
    del IObjectPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
