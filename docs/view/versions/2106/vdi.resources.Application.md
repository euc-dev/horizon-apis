---
layout: page
title: Service - Application
hide:
 #- navigation
 - toc
---

  
| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Application
See also
     [ApplicationId](vdi.entity.ApplicationId.md), [ApplicationInfo](vdi.resources.Application.ApplicationInfo.md), [ApplicationSpec](vdi.resources.Application.ApplicationSpec.md), [ApplicationSummaryView](vdi.resources.Application.ApplicationSummaryView.md), [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [MapEntry](vdi.util.MapEntry.md)
Since 
    Horizon View 6.0

  


## Service Description

Interface representing Cascadia Remote Application. 

Methods

Methods defined in this Service   
---  
Application_Create, Application_Delete, Application_DeleteApplications, Application_Get, Application_GetSummaryView, Application_GetSummaryViews, Application_ListGAECompatibleApplications, Application_Update  
  



Create a new Application 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  privilege is required to create Application.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Application](vdi.resources.Application.md) used to make the method call.   
**spec**| [ApplicationSpec](vdi.resources.Application.ApplicationSpec.md)|  The information required to create the new Application   
  
  


Return Value 

Type |  Description   
---|---  
[ApplicationId](vdi.entity.ApplicationId.md)| The id of the new Application  
  


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
VLSI_APPLICATION_CREATED|  if Application creation succeeds.   
VLSI_APPLICATION_CREATE_FAILED|  if Application creation fails.   
  
Show WSDL type definition

  
  
  



Delete a given Application. 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  privilege is required to delete the Application.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Application](vdi.resources.Application.md) used to make the method call.   
**id**| [ApplicationId](vdi.entity.ApplicationId.md)|  The entityId of the Application to delete   
  
  


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
VLSI_APPLICATION_DELETED|  if the Application is successfully deleted.   
VLSI_APPLICATION_DELETE_FAILED|  if the Application deletion failed.   
  
Show WSDL type definition

  
  
  



Delete multiple Applications. 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  privilege is required to delete the Applications.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Application](vdi.resources.Application.md) used to make the method call.   
**ids**| [ApplicationId[]](vdi.entity.ApplicationId.md)|  Array of unique identifiers for Application entries.   
  
  


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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if delete operation fails on one or more applications.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_APPLICATION_DELETED|  for every Application if it is deleted successfully   
VLSI_APPLICATION_DELETE_FAILED|  for every Application if the deletion failed   
  
Show WSDL type definition

  
  
  



Get an Application by Id. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required to get Application.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Application](vdi.resources.Application.md) used to make the method call.   
**id**| [ApplicationId](vdi.entity.ApplicationId.md)|  The entityId of the Application to get   
  
  


Return Value 

Type |  Description   
---|---  
[ApplicationInfo](vdi.resources.Application.ApplicationInfo.md)| requested Application entity  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Returns the ApplicationSummaryView for a specific Application entry. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  required to get the Application Summary View.   
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read the [applicationSummaryData](vdi.resources.Application.ApplicationSummaryView.md#applicationSummaryData).[globalApplicationEntitlement](vdi.resources.Application.ApplicationSummaryData.md#globalApplicationEntitlement) member of an application. This will be unset otherwise.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Application](vdi.resources.Application.md) used to make the method call.   
**id**| [ApplicationId](vdi.entity.ApplicationId.md)|  unique identifier for an Application entry   
  
  


Return Value 

Type |  Description   
---|---  
[ApplicationSummaryView](vdi.resources.Application.ApplicationSummaryView.md)| The ApplicationSummaryView  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Returns the ApplicationSummaryView for selected Application entries. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  required to get the Application Summary View.   
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read the [applicationSummaryData](vdi.resources.Application.ApplicationSummaryView.md#applicationSummaryData).[globalApplicationEntitlement](vdi.resources.Application.ApplicationSummaryData.md#globalApplicationEntitlement) member of an application. This will be unset otherwise.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Application](vdi.resources.Application.md) used to make the method call.   
**ids**| [ApplicationId[]](vdi.entity.ApplicationId.md)|  Array of unique identifiers for Application entries.   
  
  


Return Value 

Type |  Description   
---|---  
[ApplicationSummaryView[]](vdi.resources.Application.ApplicationSummaryView.md)| Array of ApplicationSummaryView  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



List of applications that can be associated with the specified Global Application Entitlement. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a Global Application Entitlement   
POOL_VIEW|  Desktop read privilege with the corresponding access group permission is required to read a desktop and Farm information   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Application](vdi.resources.Application.md) used to make the method call.   
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  unique identifier for Global Application Entitlement. GlobalApplicationEntitlementIds of this type must originate from [GlobalApplicationEntitlement](vdi.federation.GlobalApplicationEntitlement.md) service   
  
  


Return Value 

Type |  Description   
---|---  
[ApplicationSummaryView[]](vdi.resources.Application.ApplicationSummaryView.md)|   
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Update an Application with the set of attributes in the map. 

Privileges 

Privilege |  Description   
---|---  
POOL_ENABLE|  privilege is required to update enabled flag. POOL_MANAGEMENT privilege is required to update any other attributes.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Application](vdi.resources.Application.md) used to make the method call.   
**id**| [ApplicationId](vdi.entity.ApplicationId.md)|  The entity Id of the Application to be updated   
  
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  The key-value pairs describing attributes to be updated   


  * This parameter is an update map based on [ApplicationInfo](vdi.resources.Application.ApplicationInfo.md "ApplicationInfo"). 

  
  


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
VLSI_APPLICATION_UPDATED|  for each Application attribute that was updated.   
VLSI_APPLICATION_UPDATE_FAILED|  if the Application update failed.   
  
Show WSDL type definition

  
  
  
  
Top of page| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

