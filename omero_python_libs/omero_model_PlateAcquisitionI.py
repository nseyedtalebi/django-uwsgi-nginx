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
IceImport.load("omero_model_PlateAcquisition_ice")
from omero.rtypes import rlong
from collections import namedtuple
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class PlateAcquisitionI(_omero_model.PlateAcquisition):

      # Property Metadata
      _field_info_data = namedtuple("FieldData", ["wrapper", "nullable"])
      _field_info_type = namedtuple("FieldInfo", [
          "name",
          "startTime",
          "endTime",
          "maximumFieldCount",
          "plate",
          "wellSample",
          "annotationLinks",
          "description",
          "details",
      ])
      _field_info = _field_info_type(
          name=_field_info_data(wrapper=omero.rtypes.rstring, nullable=True),
          startTime=_field_info_data(wrapper=omero.rtypes.rtime, nullable=True),
          endTime=_field_info_data(wrapper=omero.rtypes.rtime, nullable=True),
          maximumFieldCount=_field_info_data(wrapper=omero.rtypes.rint, nullable=True),
          plate=_field_info_data(wrapper=omero.proxy_to_instance, nullable=False),
          wellSample=_field_info_data(wrapper=omero.proxy_to_instance, nullable=True),
          annotationLinks=_field_info_data(wrapper=omero.proxy_to_instance, nullable=True),
          description=_field_info_data(wrapper=omero.rtypes.rstring, nullable=True),
          details=_field_info_data(wrapper=omero.proxy_to_instance, nullable=True),
      )  # end _field_info
      NAME =  "ome.model.screen.PlateAcquisition_name"
      STARTTIME =  "ome.model.screen.PlateAcquisition_startTime"
      ENDTIME =  "ome.model.screen.PlateAcquisition_endTime"
      MAXIMUMFIELDCOUNT =  "ome.model.screen.PlateAcquisition_maximumFieldCount"
      PLATE =  "ome.model.screen.PlateAcquisition_plate"
      WELLSAMPLE =  "ome.model.screen.PlateAcquisition_wellSample"
      ANNOTATIONLINKS =  "ome.model.screen.PlateAcquisition_annotationLinks"
      DESCRIPTION =  "ome.model.screen.PlateAcquisition_description"
      DETAILS =  "ome.model.screen.PlateAcquisition_details"
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
              self._wellSampleSeq = []
              self._wellSampleLoaded = True;
          else:
              self._wellSampleSeq = []
              self._wellSampleLoaded = False;

          if load:
              self._annotationLinksSeq = []
              self._annotationLinksLoaded = True;
          else:
              self._annotationLinksSeq = []
              self._annotationLinksLoaded = False;

          pass

      def __init__(self, id=None, loaded=None):
          super(PlateAcquisitionI, self).__init__()
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
          self.unloadName( )
          self.unloadStartTime( )
          self.unloadEndTime( )
          self.unloadMaximumFieldCount( )
          self.unloadPlate( )
          self.unloadWellSample( )
          self.unloadAnnotationLinks( )
          self.unloadDescription( )
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
          return  True ;
      def isLink(self, current = None):
          return  False ;
      def shallowCopy(self, current = None):
            if not self._loaded: return self.proxy()
            copy = PlateAcquisitionI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return PlateAcquisitionI( self._id.getValue(), False )

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

      def unloadStartTime(self, ):
          self._startTimeLoaded = False
          self._startTime = None;

      def getStartTime(self, current = None):
          self.errorIfUnloaded()
          return self._startTime

      def setStartTime(self, _startTime, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.startTime.wrapper is not None:
              if _startTime is not None:
                  _startTime = self._field_info.startTime.wrapper(_startTime)
          self._startTime = _startTime
          pass

      def unloadEndTime(self, ):
          self._endTimeLoaded = False
          self._endTime = None;

      def getEndTime(self, current = None):
          self.errorIfUnloaded()
          return self._endTime

      def setEndTime(self, _endTime, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.endTime.wrapper is not None:
              if _endTime is not None:
                  _endTime = self._field_info.endTime.wrapper(_endTime)
          self._endTime = _endTime
          pass

      def unloadMaximumFieldCount(self, ):
          self._maximumFieldCountLoaded = False
          self._maximumFieldCount = None;

      def getMaximumFieldCount(self, current = None):
          self.errorIfUnloaded()
          return self._maximumFieldCount

      def setMaximumFieldCount(self, _maximumFieldCount, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.maximumFieldCount.wrapper is not None:
              if _maximumFieldCount is not None:
                  _maximumFieldCount = self._field_info.maximumFieldCount.wrapper(_maximumFieldCount)
          self._maximumFieldCount = _maximumFieldCount
          pass

      def unloadPlate(self, ):
          self._plateLoaded = False
          self._plate = None;

      def getPlate(self, current = None):
          self.errorIfUnloaded()
          return self._plate

      def setPlate(self, _plate, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.plate.wrapper is not None:
              if _plate is not None:
                  _plate = self._field_info.plate.wrapper(_plate)
          self._plate = _plate
          pass

      def unloadWellSample(self, current = None):
          self._wellSampleLoaded = False
          self._wellSampleSeq = None;

      def _getWellSample(self, current = None):
          self.errorIfUnloaded()
          return self._wellSampleSeq

      def _setWellSample(self, _wellSample, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.wellSampleSeq.wrapper is not None:
              if _wellSample is not None:
                  _wellSample = self._field_info.wellSampleSeq.wrapper(_wellSample)
          self._wellSampleSeq = _wellSample
          self.checkUnloadedProperty(_wellSample,'wellSampleLoaded')

      def isWellSampleLoaded(self):
          return self._wellSampleLoaded

      def sizeOfWellSample(self, current = None):
          self.errorIfUnloaded()
          if not self._wellSampleLoaded: return -1
          return len(self._wellSampleSeq)

      def copyWellSample(self, current = None):
          self.errorIfUnloaded()
          if not self._wellSampleLoaded: self.throwNullCollectionException("wellSampleSeq")
          return list(self._wellSampleSeq)

      def iterateWellSample(self):
          self.errorIfUnloaded()
          if not self._wellSampleLoaded: self.throwNullCollectionException("wellSampleSeq")
          return iter(self._wellSampleSeq)

      def addWellSample(self, target, current = None):
          self.errorIfUnloaded()
          if not self._wellSampleLoaded: self.throwNullCollectionException("wellSampleSeq")
          self._wellSampleSeq.append( target );
          target.setPlateAcquisition( self )

      def addAllWellSampleSet(self, targets, current = None):
          self.errorIfUnloaded()
          if  not self._wellSampleLoaded: self.throwNullCollectionException("wellSampleSeq")
          self._wellSampleSeq.extend( targets )
          for target in targets:
              target.setPlateAcquisition( self )

      def removeWellSample(self, target, current = None):
          self.errorIfUnloaded()
          if not self._wellSampleLoaded: self.throwNullCollectionException("wellSampleSeq")
          self._wellSampleSeq.remove( target )
          target.setPlateAcquisition( None )

      def removeAllWellSampleSet(self, targets, current = None):
          self.errorIfUnloaded()
          if not self._wellSampleLoaded: self.throwNullCollectionException("wellSampleSeq")
          for elt in targets:
              elt.setPlateAcquisition( None )
              self._wellSampleSeq.remove( elt )

      def clearWellSample(self, current = None):
          self.errorIfUnloaded()
          if not self._wellSampleLoaded: self.throwNullCollectionException("wellSampleSeq")
          for elt in self._wellSampleSeq:
              elt.setPlateAcquisition( None )
          self._wellSampleSeq = list()

      def reloadWellSample(self, toCopy, current = None):
          self.errorIfUnloaded()
          if self._wellSampleLoaded:
              raise omero.ClientError("Cannot reload active collection: wellSampleSeq")
          if not toCopy:
              raise omero.ClientError("Argument cannot be null")
          if toCopy.getId().getValue() != self.getId().getValue():
             raise omero.ClientError("Argument must have the same id as this instance")
          if toCopy.getDetails().getUpdateEvent().getId().getValue() < self.getDetails().getUpdateEvent().getId().getValue():
             raise omero.ClientError("Argument may not be older than this instance")
          copy = toCopy.copyWellSample() # May also throw
          for elt in copy:
              elt.setPlateAcquisition( self )
          self._wellSampleSeq = copy
          toCopy.unloadWellSample()
          self._wellSampleLoaded = True

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

      def addPlateAcquisitionAnnotationLink(self, target, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.append( target );
          target.setParent( self )

      def addAllPlateAcquisitionAnnotationLinkSet(self, targets, current = None):
          self.errorIfUnloaded()
          if  not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.extend( targets )
          for target in targets:
              target.setParent( self )

      def removePlateAcquisitionAnnotationLink(self, target, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.remove( target )
          target.setParent( None )

      def removeAllPlateAcquisitionAnnotationLinkSet(self, targets, current = None):
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
          link = _omero_model.PlateAcquisitionAnnotationLinkI()
          link.link( self, addition );
          self.addPlateAcquisitionAnnotationLinkToBoth( link, True )
          return link

      def addPlateAcquisitionAnnotationLinkToBoth(self, link, bothSides):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          self._annotationLinksSeq.append( link )

      def findPlateAcquisitionAnnotationLink(self, removal, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          result = list()
          for link in self._annotationLinksSeq:
              if link.getChild() == removal: result.append(link)
          return result

      def unlinkAnnotation(self, removal, current = None):
          self.errorIfUnloaded()
          if not self._annotationLinksLoaded: self.throwNullCollectionException("annotationLinksSeq")
          toRemove = self.findPlateAcquisitionAnnotationLink(removal)
          for next in toRemove:
              self.removePlateAcquisitionAnnotationLinkFromBoth( next, True )

      def removePlateAcquisitionAnnotationLinkFromBoth(self, link, bothSides, current = None):
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

      def unloadDescription(self, ):
          self._descriptionLoaded = False
          self._description = None;

      def getDescription(self, current = None):
          self.errorIfUnloaded()
          return self._description

      def setDescription(self, _description, current = None, wrap=False):
          self.errorIfUnloaded()
          if wrap and self._field_info.description.wrapper is not None:
              if _description is not None:
                  _description = self._field_info.description.wrapper(_description)
          self._description = _description
          pass


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

_omero_model.PlateAcquisitionI = PlateAcquisitionI
