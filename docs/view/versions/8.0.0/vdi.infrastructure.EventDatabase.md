---
layout: page
title: Service - EventDatabase
hide:
 #- navigation
 - toc
---

  
 
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.EventDatabase`

See also  
> [EventDatabaseInfo](vdi.infrastructure.EventDatabase.EventDatabaseInfo.md), [MapEntry](vdi.util.MapEntry.md)

Since  
> Horizon View 6.0


  


## Service Description

Service to manage the event database. 

Methods

Methods defined in this Service   
---  
EventDatabase_Clear, EventDatabase_Get, EventDatabase_Update  
  



Clear the event database settings for this View cluster. If no event database is set, this will no-op. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global management is required to clear event database settings.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [EventDatabase](vdi.infrastructure.EventDatabase.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_DATABASE_CONFIGURATION_DELETED|  If a set Event Database was successfully cleared.   
ADMIN_DATABASE_CONFIGURATION_DELETE_FAILED|  If a set Event Database could not be cleared.   
  
Show WSDL type definition

  
  
  



Gets the event database settings for this View cluster If no event database is set, the eventDatabaseSet field will indicate that the settings and database members should be ignored. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get event database settings.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [EventDatabase](vdi.infrastructure.EventDatabase.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[EventDatabaseInfo](vdi.infrastructure.EventDatabase.EventDatabaseInfo.md)| The GlobalSettingsInfo object.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Updates the event database settings for this View cluster. If no event database is set, this will cause a new event database to be set. If the settings are invalid, will throw InvalidRequest. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global management is required to update event database settings.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [EventDatabase](vdi.infrastructure.EventDatabase.md) used to make the method call.   
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated   


  * This parameter is an update map based on [EventDatabaseInfo](vdi.infrastructure.EventDatabase.EventDatabaseInfo.md "EventDatabaseInfo"). 

  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if the broker can't connect to the database with the new settings  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_DATABASE_CONFIGURATION_ADDED|  If the Event Database was not set, and a new one was successfully created.   
ADMIN_DATABASE_CONFIGURATION_ADD_FAILED|  If the Event Data was not set, and a new one could not be created.   
ADMIN_DATABASE_CONFIGURATION_UPDATED|  If a set Event Database was successfully updated.   
ADMIN_DATABASE_CONFIGURATION_UPDATE_FAILED|  If a set Event Database could not be updated.   
  
Show WSDL type definition

  
  
  
  
  
  
  
