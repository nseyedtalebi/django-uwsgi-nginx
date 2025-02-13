"""
   /*
   **   Generated by blitz/resources/templates/combined.vm
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
"""
import Ice
import IceImport
import omero
IceImport.load("omero_model_DetailsI")
IceImport.load("omero_model_RenderingDef_ice")
from omero.rtypes import rlong
from collections import namedtuple
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class RenderingDefI(_omero_model.RenderingDef):

      # Property Metadata
      _field_info_data = namedtuple("FieldData", ["wrapper", "nullable"])
      _field_info_type = namedtuple("FieldInfo", [
          "pixels",
          "defaultZ",
          "defaultT",
          "model",
          "waveRendering",
          "name",
          "compression",
          "quantization",
          "projections",
          "details",
      ])
      _field_info = _field_info_type(
          pixels=_field_info_data(wrapper=omero.proxy_to_instance, nullable=False),
          defaultZ=_field_info_data(wrapper=omero.rtypes.rint, nullable=False),
          defaultT=_field_info_data(wrapper=omero.rtypes.rint, nullable=False),
          model=_field_info_data(wrapper=omero.proxy_to_instance, nullable=False),
          waveRendering=_field_info_data(wrapper=omero.proxy_to_instance, nullable=False),
          name=_field_info_data(wrapper=omero.rtypes.rstring, nullable=True),
          compression=_field_info_data(wrapper=omero.rtypes.rdouble, nullable=True),
          quantization=_field_info_data(wrapper=omero.proxy_to_instance, nullable=False),
          projections=_field_info_data(wrapper=omero.proxy_to_instance, nullable=False),
          details=_field_info_data(wrapper=omero.proxy_to_instance, nullable=True),
      )  # end _field_info
      PIXELS =  "ome.model.display.RenderingDef_pixels"
      DEFAULTZ =  "ome.model.display.RenderingDef_defaultZ"
      DEFAULTT =  "ome.model.display.RenderingDef_defaultT"
      MODEL =  "ome.model.display.RenderingDef_model"
      WAVERENDERING =  "ome.model.display.RenderingDef_waveRendering"
      NAME =  "ome.model.display.RenderingDef_name"
      COMPRESSION =  "ome.model.display.RenderingDef_compression"
      QUANTIZATION =  "ome.model.display.RenderingDef_quantization"
      PROJECTIONS =  "ome.model.display.RenderingDef_projections"
      DETAILS =  "ome.model.display.RenderingDef_details"
      def errorIfUnloaded(self):
          if not self._loaded:
              raise _omero.UnloadedEntityException("Object unloaded:"+str(self))

      def throwNullCollectionException(self,propertyName):
          raise _omero.UnloadedEntityException(""+
          "Error updating collection:" + propertyName +"\n"+
          "Collection is currently null. This can be seen\n" +
          "by testing \""+ propertyName +"Loaded\". This implies\n"+
          "that this collection was unloaded. Please refresh this object\n"+
          "in order to update this collection.\n")

      def _toggleCollectionsLoaded(self, load):
          if load:
              self._waveRenderingSeq = []
              self._waveRenderingLoaded = True;
          else:
              self._waveRenderingSeq = []
              self._waveRenderingLoaded = False;

          if load:
              self._projectionsSeq = []
              self._projectionsLoaded = True;
          else:
              self._projectionsSeq = []
              self._projectionsLoaded = False;

          pass

      def __init__(self, id=None, loaded=None):
          super(RenderingDefI, self).__init__()
          if id is not None and isinstance(id, (str, unicode)) and ":" in id:
              parts = id.split(":")
              if len(parts) != 2:
                  raise Exception("Invalid proxy string: %s", id)
              if parts[0] != self.__class__.__name__ and \
                 parts[0]+"I" != self.__class__.__name__:
                  raise Exception("Proxy class mismatch: %s<>%s" %
                  (self.__class__.__name__, parts[0]))
              self._id = rlong(parts[1])
              if loaded is None:
                  # If no loadedness was requested with
                  # a proxy string, then assume False.
                  loaded = False
          else:
              # Relying on omero.rtypes.rlong's error-handling
              self._id = rlong(id)
              if loaded is None:
                  loaded = True  # Assume true as previously
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadPixels( )
          self.unloadDefaultZ( )
          self.unloadDefaultT( )
          self.unloadModel( )
          self.unloadWaveRendering( )
          self.unloadName( )
          self.unloadCompression( )
          self.unloadQuantization( )
          self.unloadProjections( )
          self.unloadDetails( )

      def isLoaded(self, current = None):
          return self._loaded
      def unloadCollections(self, current = None):
          self._toggleCollectionsLoaded( False )
      def isGlobal(self, current = None):
          return  False ;
      def isMutable(self, current = None):
          return  True ;
      def isAnnotated(self, current = None):
          return  False ;
      def isLink(self, current = None):
          return  False ;
      def shallowCopy(self, current = None):
            if not self._loaded: return self.proxy()
            copy = RenderingDefI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return RenderingDefI( self._id.getValue(), False )

      def getDetails(self, current = None):
          self.errorIfUnloaded()
          return self._details

      def unloadDetails(self, current = None):
          self._details = None

      def getId(self, current = None):
          return self._id

      def setId(self, _id, current = None):
          self._id = _id

      def checkUnloadedProperty(self, value, loadedField):
          if value == None:
              self.__dict__[loadedField] = False
          else:
              self.__dict__[loadedField] = True

      def getVersion(self, current = None):
          self.errorIfUnloaded()
          return self._version

      def setVersion(self, version, current = None):
          self.errorIfUnloaded()
          self._version = version

      def unloadPixels(self, ):
          self._pixelsLoaded = False
          self._pixels = None;

      def getPixels(self, current = None):
          self.errorIfUnloaded()
          return self._pixels

      def setPixels(self, _pixels, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.pixels.wrapper is not None:
              if _pixels is not None:
                  _pixels = self._field_info.pixels.wrapper(_pixels)
          self._pixels = _pixels
          pass

      def unloadDefaultZ(self, ):
          self._defaultZLoaded = False
          self._defaultZ = None;

      def getDefaultZ(self, current = None):
          self.errorIfUnloaded()
          return self._defaultZ

      def setDefaultZ(self, _defaultZ, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.defaultZ.wrapper is not None:
              if _defaultZ is not None:
                  _defaultZ = self._field_info.defaultZ.wrapper(_defaultZ)
          self._defaultZ = _defaultZ
          pass

      def unloadDefaultT(self, ):
          self._defaultTLoaded = False
          self._defaultT = None;

      def getDefaultT(self, current = None):
          self.errorIfUnloaded()
          return self._defaultT

      def setDefaultT(self, _defaultT, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.defaultT.wrapper is not None:
              if _defaultT is not None:
                  _defaultT = self._field_info.defaultT.wrapper(_defaultT)
          self._defaultT = _defaultT
          pass

      def unloadModel(self, ):
          self._modelLoaded = False
          self._model = None;

      def getModel(self, current = None):
          self.errorIfUnloaded()
          return self._model

      def setModel(self, _model, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.model.wrapper is not None:
              if _model is not None:
                  _model = self._field_info.model.wrapper(_model)
          self._model = _model
          pass

      def unloadWaveRendering(self, current = None):
          self._waveRenderingLoaded = False
          self._waveRenderingSeq = None;

      def _getWaveRendering(self, current = None):
          self.errorIfUnloaded()
          return self._waveRenderingSeq

      def _setWaveRendering(self, _waveRendering, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.waveRenderingSeq.wrapper is not None:
              if _waveRendering is not None:
                  _waveRendering = self._field_info.waveRenderingSeq.wrapper(_waveRendering)
          self._waveRenderingSeq = _waveRendering
          self.checkUnloadedProperty(_waveRendering,'waveRenderingLoaded')

      def isWaveRenderingLoaded(self):
          return self._waveRenderingLoaded

      def sizeOfWaveRendering(self, current = None):
          self.errorIfUnloaded()
          if not self._waveRenderingLoaded: return -1
          return len(self._waveRenderingSeq)

      def copyWaveRendering(self, current = None):
          self.errorIfUnloaded()
          if not self._waveRenderingLoaded: self.throwNullCollectionException("waveRenderingSeq")
          return list(self._waveRenderingSeq)

      def iterateWaveRendering(self):
          self.errorIfUnloaded()
          if not self._waveRenderingLoaded: self.throwNullCollectionException("waveRenderingSeq")
          return iter(self._waveRenderingSeq)

      def addChannelBinding(self, target, current = None):
          self.errorIfUnloaded()
          if not self._waveRenderingLoaded: self.throwNullCollectionException("waveRenderingSeq")
          self._waveRenderingSeq.append( target );
          target.setRenderingDef( self )

      def addAllChannelBindingSet(self, targets, current = None):
          self.errorIfUnloaded()
          if  not self._waveRenderingLoaded: self.throwNullCollectionException("waveRenderingSeq")
          self._waveRenderingSeq.extend( targets )
          for target in targets:
              target.setRenderingDef( self )

      def removeChannelBinding(self, target, current = None):
          self.errorIfUnloaded()
          if not self._waveRenderingLoaded: self.throwNullCollectionException("waveRenderingSeq")
          self._waveRenderingSeq.remove( target )
          target.setRenderingDef( None )

      def removeAllChannelBindingSet(self, targets, current = None):
          self.errorIfUnloaded()
          if not self._waveRenderingLoaded: self.throwNullCollectionException("waveRenderingSeq")
          for elt in targets:
              elt.setRenderingDef( None )
              self._waveRenderingSeq.remove( elt )

      def clearWaveRendering(self, current = None):
          self.errorIfUnloaded()
          if not self._waveRenderingLoaded: self.throwNullCollectionException("waveRenderingSeq")
          for elt in self._waveRenderingSeq:
              elt.setRenderingDef( None )
          self._waveRenderingSeq = list()

      def reloadWaveRendering(self, toCopy, current = None):
          self.errorIfUnloaded()
          if self._waveRenderingLoaded:
              raise omero.ClientError("Cannot reload active collection: waveRenderingSeq")
          if not toCopy:
              raise omero.ClientError("Argument cannot be null")
          if toCopy.getId().getValue() != self.getId().getValue():
             raise omero.ClientError("Argument must have the same id as this instance")
          if toCopy.getDetails().getUpdateEvent().getId().getValue() < self.getDetails().getUpdateEvent().getId().getValue():
             raise omero.ClientError("Argument may not be older than this instance")
          copy = toCopy.copyWaveRendering() # May also throw
          for elt in copy:
              elt.setRenderingDef( self )
          self._waveRenderingSeq = copy
          toCopy.unloadWaveRendering()
          self._waveRenderingLoaded = True

      def getChannelBinding(self, index, current = None):
          self.errorIfUnloaded()
          if not self._waveRenderingLoaded: self.throwNullCollectionException("waveRenderingSeq")
          return self._waveRenderingSeq[index]

      def setChannelBinding(self, index, element, current = None, wrap=False):
          self.errorIfUnloaded()
          if not self._waveRenderingLoaded: self.throwNullCollectionException("waveRenderingSeq")
          old = self._waveRenderingSeq[index]
          if wrap and self._field_info.waveRenderingSeq.wrapper is not None:
              if element is not None:
                  element = self._field_info.waveRenderingSeq.wrapper(_waveRendering)
          self._waveRenderingSeq[index] =  element
          if element is not None and element.isLoaded():
              element.setRenderingDef( self )
          return old

      def getPrimaryChannelBinding(self, current = None):
          self.errorIfUnloaded()
          if not self._waveRenderingLoaded: self.throwNullCollectionException("waveRenderingSeq")
          return self._waveRenderingSeq[0]

      def setPrimaryChannelBinding(self, element, current = None):
          self.errorIfUnloaded()
          if not self._waveRenderingLoaded: self.throwNullCollectionException("waveRenderingSeq")
          index = self._waveRenderingSeq.index(element)
          old = self._waveRenderingSeq[0]
          self._waveRenderingSeq[index] = old
          self._waveRenderingSeq[0] = element
          return old

      def unloadName(self, ):
          self._nameLoaded = False
          self._name = None;

      def getName(self, current = None):
          self.errorIfUnloaded()
          return self._name

      def setName(self, _name, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.name.wrapper is not None:
              if _name is not None:
                  _name = self._field_info.name.wrapper(_name)
          self._name = _name
          pass

      def unloadCompression(self, ):
          self._compressionLoaded = False
          self._compression = None;

      def getCompression(self, current = None):
          self.errorIfUnloaded()
          return self._compression

      def setCompression(self, _compression, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.compression.wrapper is not None:
              if _compression is not None:
                  _compression = self._field_info.compression.wrapper(_compression)
          self._compression = _compression
          pass

      def unloadQuantization(self, ):
          self._quantizationLoaded = False
          self._quantization = None;

      def getQuantization(self, current = None):
          self.errorIfUnloaded()
          return self._quantization

      def setQuantization(self, _quantization, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.quantization.wrapper is not None:
              if _quantization is not None:
                  _quantization = self._field_info.quantization.wrapper(_quantization)
          self._quantization = _quantization
          pass

      def unloadProjections(self, current = None):
          self._projectionsLoaded = False
          self._projectionsSeq = None;

      def _getProjections(self, current = None):
          self.errorIfUnloaded()
          return self._projectionsSeq

      def _setProjections(self, _projections, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.projectionsSeq.wrapper is not None:
              if _projections is not None:
                  _projections = self._field_info.projectionsSeq.wrapper(_projections)
          self._projectionsSeq = _projections
          self.checkUnloadedProperty(_projections,'projectionsLoaded')

      def isProjectionsLoaded(self):
          return self._projectionsLoaded

      def sizeOfProjections(self, current = None):
          self.errorIfUnloaded()
          if not self._projectionsLoaded: return -1
          return len(self._projectionsSeq)

      def copyProjections(self, current = None):
          self.errorIfUnloaded()
          if not self._projectionsLoaded: self.throwNullCollectionException("projectionsSeq")
          return list(self._projectionsSeq)

      def iterateProjections(self):
          self.errorIfUnloaded()
          if not self._projectionsLoaded: self.throwNullCollectionException("projectionsSeq")
          return iter(self._projectionsSeq)

      def addProjectionDef(self, target, current = None):
          self.errorIfUnloaded()
          if not self._projectionsLoaded: self.throwNullCollectionException("projectionsSeq")
          self._projectionsSeq.append( target );
          target.setRenderingDef( self )

      def addAllProjectionDefSet(self, targets, current = None):
          self.errorIfUnloaded()
          if  not self._projectionsLoaded: self.throwNullCollectionException("projectionsSeq")
          self._projectionsSeq.extend( targets )
          for target in targets:
              target.setRenderingDef( self )

      def removeProjectionDef(self, target, current = None):
          self.errorIfUnloaded()
          if not self._projectionsLoaded: self.throwNullCollectionException("projectionsSeq")
          self._projectionsSeq.remove( target )
          target.setRenderingDef( None )

      def removeAllProjectionDefSet(self, targets, current = None):
          self.errorIfUnloaded()
          if not self._projectionsLoaded: self.throwNullCollectionException("projectionsSeq")
          for elt in targets:
              elt.setRenderingDef( None )
              self._projectionsSeq.remove( elt )

      def clearProjections(self, current = None):
          self.errorIfUnloaded()
          if not self._projectionsLoaded: self.throwNullCollectionException("projectionsSeq")
          for elt in self._projectionsSeq:
              elt.setRenderingDef( None )
          self._projectionsSeq = list()

      def reloadProjections(self, toCopy, current = None):
          self.errorIfUnloaded()
          if self._projectionsLoaded:
              raise omero.ClientError("Cannot reload active collection: projectionsSeq")
          if not toCopy:
              raise omero.ClientError("Argument cannot be null")
          if toCopy.getId().getValue() != self.getId().getValue():
             raise omero.ClientError("Argument must have the same id as this instance")
          if toCopy.getDetails().getUpdateEvent().getId().getValue() < self.getDetails().getUpdateEvent().getId().getValue():
             raise omero.ClientError("Argument may not be older than this instance")
          copy = toCopy.copyProjections() # May also throw
          for elt in copy:
              elt.setRenderingDef( self )
          self._projectionsSeq = copy
          toCopy.unloadProjections()
          self._projectionsLoaded = True

      def getProjectionDef(self, index, current = None):
          self.errorIfUnloaded()
          if not self._projectionsLoaded: self.throwNullCollectionException("projectionsSeq")
          return self._projectionsSeq[index]

      def setProjectionDef(self, index, element, current = None, wrap=False):
          self.errorIfUnloaded()
          if not self._projectionsLoaded: self.throwNullCollectionException("projectionsSeq")
          old = self._projectionsSeq[index]
          if wrap and self._field_info.projectionsSeq.wrapper is not None:
              if element is not None:
                  element = self._field_info.projectionsSeq.wrapper(_projections)
          self._projectionsSeq[index] =  element
          if element is not None and element.isLoaded():
              element.setRenderingDef( self )
          return old

      def getPrimaryProjectionDef(self, current = None):
          self.errorIfUnloaded()
          if not self._projectionsLoaded: self.throwNullCollectionException("projectionsSeq")
          return self._projectionsSeq[0]

      def setPrimaryProjectionDef(self, element, current = None):
          self.errorIfUnloaded()
          if not self._projectionsLoaded: self.throwNullCollectionException("projectionsSeq")
          index = self._projectionsSeq.index(element)
          old = self._projectionsSeq[0]
          self._projectionsSeq[index] = old
          self._projectionsSeq[0] = element
          return old


      def ice_postUnmarshal(self):
          """
          Provides additional initialization once all data loaded
          """
          pass # Currently unused


      def ice_preMarshal(self):
          """
          Provides additional validation before data is sent
          """
          pass # Currently unused

      def __getattr__(self, name):
          import __builtin__
          """
          Reroutes all access to object.field through object.getField() or object.isField()
          """
          if "_" in name:  # Ice disallows underscores, so these should be treated normally.
              return object.__getattribute__(self, name)
          field  = "_" + name
          capitalized = name[0].capitalize() + name[1:]
          getter = "get" + capitalized
          questn = "is" + capitalized
          try:
              self.__dict__[field]
              if hasattr(self, getter):
                  method = getattr(self, getter)
                  return method()
              elif hasattr(self, questn):
                  method = getattr(self, questn)
                  return method()
          except:
              pass
          raise AttributeError("'%s' object has no attribute '%s' or '%s'" % (self.__class__.__name__, getter, questn))

      def __setattr__(self, name, value):
          """
          Reroutes all access to object.field through object.getField(), with the caveat
          that all sets on variables starting with "_" are permitted directly.
          """
          if name.startswith("_"):
              self.__dict__[name] = value
              return
          else:
              field  = "_" + name
              setter = "set" + name[0].capitalize() + name[1:]
              if hasattr(self, field) and hasattr(self, setter):
                  method = getattr(self, setter)
                  return method(value)
          raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, setter))

_omero_model.RenderingDefI = RenderingDefI
