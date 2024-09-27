---
layout: page
title: Service - URLRedirection
hide:
 #- navigation
 - toc
---

  
   
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.URLRedirection  
See also
     [MapEntry](vdi.util.MapEntry.md), [URLRedirectionId](vdi.entity.URLRedirectionId.md), [URLRedirectionInfo](vdi.infrastructure.URLRedirection.URLRedirectionInfo.md), [URLRedirectionSpec](vdi.infrastructure.URLRedirection.URLRedirectionSpec.md)  
Since 
    Horizon 7.0

  


## Service Description

Service Interface for URLRedirection Setting. 

Methods

Methods defined in this Service   
---  
URLRedirection_Create, URLRedirection_Delete, URLRedirection_Get, URLRedirection_List, URLRedirection_Update  
  



Create a new URLRedirection Setting. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global config management privilege is required to create a URLRedirection setting.   
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to create a global URLRedirection setting.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [URLRedirection](vdi.infrastructure.URLRedirection.md) used to make the method call.   
**urlRedirectionSpec**| [URLRedirectionSpec](vdi.infrastructure.URLRedirection.URLRedirectionSpec.md)|    
  
  


Return Value 

Type |  Description   
---|---  
[URLRedirectionId](vdi.entity.URLRedirectionId.md)| The id of the new URLRedirection Setting.  
  


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
VLSI_URL_REDIRECTION_CREATED|  if URLRedirection creation succeeds.   
VLSI_URL_REDIRECTION_CREATE_FAILED|  if URLRedirection creation fails.   
  
Show WSDL type definition

  
  
  



Delete a given URLRedirection Setting. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global config management privilege is required to delete a URLRedirection setting.   
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to delete a global URLRedirection setting.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [URLRedirection](vdi.infrastructure.URLRedirection.md) used to make the method call.   
**id**| [URLRedirectionId](vdi.entity.URLRedirectionId.md)|  The entityId of the URLRedirection to be deleted.   
  
  


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
VLSI_URL_REDIRECTION_DELETED|  if the URLRedirection is successfully deleted.   
VLSI_URL_REDIRECTION_DELETE_FAILED|  if the URLRedirection deletion failed.   
  
Show WSDL type definition

  
  
  



Get a URLRedirection Setting by Id. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global config view privilege is required to read a URLRedirection setting.   
FEDERATED_LDAP_VIEW|  Global LDAP view is required to read a global URLRedirection setting.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [URLRedirection](vdi.infrastructure.URLRedirection.md) used to make the method call.   
**id**| [URLRedirectionId](vdi.entity.URLRedirectionId.md)|  The entityId of the URLRedirection to get.   
  
  


Return Value 

Type |  Description   
---|---  
[URLRedirectionInfo](vdi.infrastructure.URLRedirection.URLRedirectionInfo.md)| requested URLRedirectionInfo entity  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



List the configured URLRedirection Settings. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global config view privilege is required to list all URLRedirection settings.   
FEDERATED_LDAP_VIEW|  Global LDAP view is required to list all URLRedirection settings.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [URLRedirection](vdi.infrastructure.URLRedirection.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[URLRedirectionInfo[]](vdi.infrastructure.URLRedirection.URLRedirectionInfo.md)|   
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Update the URLRedirection with the set of attributes in the map. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global config management privilege is required to update a URLRedirection setting.   
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update a global URLRedirection setting.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [URLRedirection](vdi.infrastructure.URLRedirection.md) used to make the method call.   
**id**| [URLRedirectionId](vdi.entity.URLRedirectionId.md)|  The entityId of the URLRedirection to be updated.   
  
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  The key-value pairs describing attributes to be updated.   


  * This parameter is an update map based on [URLRedirectionInfo](vdi.infrastructure.URLRedirection.URLRedirectionInfo.md "URLRedirectionInfo"). 

  
  


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
VLSI_URL_REDIRECTION_UPDATED|  for each URLRedirection attribute that was updated.   
VLSI_URL_REDIRECTION_UPDATE_FAILED|  if URLRedirection update failed.   
  
Show WSDL type definition

  
  
  
  
  
  
  

