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
IceImport.load("omero_model_Arc_ice")
from omero.rtypes import rlong
from collections import namedtuple
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class ArcI(_omero_model.Arc):

      # Property Metadata
      _field_info_data = namedtuple("FieldData", ["wrapper", "nullable"])
      _field_info_type = namedtuple("FieldInfo", [
          "type",
          "manufacturer",
          "model",
          "power",
          "lotNumber",
          "serialNumber",
          "instrument",
          "annotationLinks",
          "details",
      ])
      _field_info = _field_info_type(
          type=_field_info_data(wrapper=omero.proxy_to_instance, nullable=False),
          manufacturer=_field_info_data(wrapper=omero.rtypes.rstring, nullable=True),
          model=_field_info_data(wrapper=omero.rtypes.rstring, nullable=True),
          power=_field_info_data(wrapper=omero.proxy_to_instance, nullable=True),
          lotNumber=_field_info_data(wrapper=omero.rtypes.rstring, nullable=True),
          serialNumber=_field_info_data(wrapper=omero.rtypes.rstring, nullable=True),
          instrument=_field_info_data(wrapper=omero.proxy_to_instance, nullable=False),
          annotationLinks=_field_info_data(wrapper=omero.proxy_to_instance, nullable=True),
          details=_field_info_data(wrapper=omero.proxy_to_instance, nullable=True),
      )  # end _field_info
      TYPE =  "ome.model.acquisition.Arc_type"
      MANUFACTURER =  "ome.model.acquisition.Arc_manufacturer"
      MODEL =  "ome.model.acquisition.Arc_model"
      POWER =  "ome.model.acquisition.Arc_power"
      LOTNUMBER =  "ome.model.acquisition.Arc_lotNumber"
      SERIALNUMBER =  "ome.model.acquisition.Arc_serialNumber"
      INSTRUMENT =  "ome.model.acquisition.Arc_instrument"
      ANNOTATIONLINKS =  "ome.model.acquisition.Arc_annotationLinks"
      DETAILS =  "ome.model.acquisition.Arc_details"
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
              self._annotationLinksSeq = []
              self._annotationLinksLoaded = True;
          else:
              self._annotationLinksSeq = []
              self._annotationLinksLoaded = False;

          pass

      def __init__(self, id=None, loaded=None):
          super(ArcI, self).__init__()
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
          self.unloadType( )
          self.unloadManufacturer( )
          self.unloadModel( )
          self.unloadPower( )
          self.unloadLotNumber( )
          self.unloadSerialNumber( )
          self.unloadInstrument( )
          self.unloadAnnotationLinks( )
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
            copy = ArcI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return ArcI( self._id.getValue(), False )

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

      def unloadType(self, ):
          self._typeLoaded = False
          self._type = None;

      def getType(self, current = None):
          self.errorIfUnloaded()
          return self._type

      def setType(self, _type, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.type.wrapper is not None:
              if _type is not None:
                  _type = self._field_info.type.wrapper(_type)
          self._type = _type
          pass

      def unloadManufacturer(self, ):
          self._manufacturerLoaded = False
          self._manufacturer = None;

      def getManufacturer(self, current = None):
          self.errorIfUnloaded()
          return self._manufacturer

      def setManufacturer(self, _manufacturer, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.manufacturer.wrapper is not None:
              if _manufacturer is not None:
                  _manufacturer = self._field_info.manufacturer.wrapper(_manufacturer)
          self._manufacturer = _manufacturer
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

      def unloadPower(self, ):
          self._powerLoaded = False
          self._power = None;

      def getPower(self, current = None):
          self.errorIfUnloaded()
          return self._power

      def setPower(self, _power, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.power.wrapper is not None:
              if _power is not None:
                  _power = self._field_info.power.wrapper(_power)
          self._power = _power
          pass

      def unloadLotNumber(self, ):
          self._lotNumberLoaded = False
          self._lotNumber = None;

      def getLotNumber(self, current = None):
          self.errorIfUnloaded()
          return self._lotNumber

      def setLotNumber(self, _lotNumber, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.lotNumber.wrapper is not None:
              if _lotNumber is not None:
                  _lotNumber = self._field_info.lotNumber.wrapper(_lotNumber)
          self._lotNumber = _lotNumber
          pass

      def unloadSerialNumber(self, ):
          self._serialNumberLoaded = False
          self._serialNumber = None;

      def getSerialNumber(self, current = None):
          self.errorIfUnloaded()
          return self._serialNumber

      def setSerialNumber(self, _serialNumber, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.serialNumber.wrapper is not None:
              if _serialNumber is not None:
                  _serialNumber = self._field_info.serialNumber.wrapper(_serialNumber)
          self._serialNumber = _serialNumber
          pass

      def unloadInstrument(self, ):
          self._instrumentLoaded = False
          self._instrument = None;

      def getInstrument(self, current = None):
          self.errorIfUnloaded()
          return self._instrument

      def setInstrument(self, _instrument, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.instrument.wrapper is not None:
              if _instrument is not None:
                  _instrument = self._field_info.instrument.wrapper(_instrument)
          self._instrument = _instrument
          pass

      def unloadAnnotationLinks(self, current = None):
          self._annotationLinksLoaded = False
          self._annotationLinksSeq = None;

      def _getAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          return self._annotationLinksSeq

      def _setAnnotationLinks(self, _annotationLinks, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.annotationLinksSeq.wrapper is not None:
              if _annotationLinks is not None:
                  _annotationLinks = self._field_info.annotationLinksSeq.wrapper(_annotationLinks)
          self._annotationLinksSeq = _annotationLinks
          self.checkUnloadedProperty(_annotationLinks,'annotationLinksLoaded')

      def isAnnotationLinksLoaded(self):
          return self._annotationLinksLoaded

      def sizeOfAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: return -1
          return len(self._annotationLinksSeq)

      def copyAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          return list(self._annotationLinksSeq)

      def iterateAnnotationLinks(self):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          return iter(self._annotationLinksSeq)

      def addLightSourceAnnotationLink(self, target, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.append( target );
          target.setParent( self )

      def addAllLightSourceAnnotationLinkSet(self, targets, current = None):
          self.errorIfUnloaded()
          if  not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.extend( targets )
          for target in targets:
              target.setParent( self )

      def removeLightSourceAnnotationLink(self, target, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.remove( target )
          target.setParent( None )

      def removeAllLightSourceAnnotationLinkSet(self, targets, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          for elt in targets:
              elt.setParent( None )
              self._annotationLinksSeq.remove( elt )

      def clearAnnotationLinks(self, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          for elt in self._annotationLinksSeq:
              elt.setParent( None )
          self._annotationLinksSeq = list()

      def reloadAnnotationLinks(self, toCopy, current = None):
          self.errorIfUnloaded()
          if self._annotationLinksLoaded:
              raise omero.ClientError("Cannot reload active collection: annotationLinksSeq")
          if not toCopy:
              raise omero.ClientError("Argument cannot be null")
          if toCopy.getId().getValue() != self.getId().getValue():
             raise omero.ClientError("Argument must have the same id as this instance")
          if toCopy.getDetails().getUpdateEvent().getId().getValue() < self.getDetails().getUpdateEvent().getId().getValue():
             raise omero.ClientError("Argument may not be older than this instance")
          copy = toCopy.copyAnnotationLinks() # May also throw
          for elt in copy:
              elt.setParent( self )
          self._annotationLinksSeq = copy
          toCopy.unloadAnnotationLinks()
          self._annotationLinksLoaded = True

      def getAnnotationLinksCountPerOwner(self, current = None):
          return self._annotationLinksCountPerOwner

      def linkAnnotation(self, addition, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          link = _omero_model.LightSourceAnnotationLinkI()
          link.link( self, addition );
          self.addLightSourceAnnotationLinkToBoth( link, True )
          return link

      def addLightSourceAnnotationLinkToBoth(self, link, bothSides):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.append( link )

      def findLightSourceAnnotationLink(self, removal, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          result = list()
          for link in self._annotationLinksSeq:
              if link.getChild() == removal: result.append(link)
          return result

      def unlinkAnnotation(self, removal, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          toRemove = self.findLightSourceAnnotationLink(removal)
          for next in toRemove:
              self.removeLightSourceAnnotationLinkFromBoth( next, True )

      def removeLightSourceAnnotationLinkFromBoth(self, link, bothSides, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.remove( link )

      def linkedAnnotationList(self, current = None):
          self.errorIfUnloaded()
          if not self.annotationLinksLoaded: self.throwNullCollectionException("AnnotationLinks")
          linked = []
          for link in self._annotationLinksSeq:
              linked.append( link.getChild() )
          return linked


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

_omero_model.ArcI = ArcI
