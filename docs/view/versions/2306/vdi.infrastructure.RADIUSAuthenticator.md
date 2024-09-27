---
layout: page
title: Service - RADIUSAuthenticator
hide:
 #- navigation
 - toc
---

  
  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.RADIUSAuthenticator  
See also
     [MapEntry](vdi.util.MapEntry.md), [RADIUSAuthenticatorId](vdi.entity.RADIUSAuthenticatorId.md), [RADIUSAuthenticatorInfo](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorInfo.md), [RADIUSAuthenticatorSpec](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorSpec.md)  
Since 
    Horizon View 6.0

  


## Service Description

Service for managing RADIUS authenticators. 

Methods

Methods defined in this Service   
---  
RADIUSAuthenticator_Create, RADIUSAuthenticator_Delete, RADIUSAuthenticator_Get, RADIUSAuthenticator_List, RADIUSAuthenticator_Update  
  



Creates a RADIUS authenticator. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to create a RADIUS authenticator.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RADIUSAuthenticator](vdi.infrastructure.RADIUSAuthenticator.md) used to make the method call.   
**spec**| [RADIUSAuthenticatorSpec](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorSpec.md)|  The specification of the RADIUS authenticator.   
  
  


Return Value 

Type |  Description   
---|---  
[RADIUSAuthenticatorId](vdi.entity.RADIUSAuthenticatorId.md)| The ID of the newly created RADIUS authenticator.  
  


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
VLSI_RADIUS_AUTHENTICATOR_CREATED|  If the RADIUS authenticator was successfully created.   
VLSI_RADIUS_AUTHENTICATOR_CREATE_FAILED|  If the RADIUS authenticator could not be created.   
  
Show WSDL type definition

  
  
  



Deletes the specified RADIUS authenticator. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete a RADIUS authenticator.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RADIUSAuthenticator](vdi.infrastructure.RADIUSAuthenticator.md) used to make the method call.   
**id**| [RADIUSAuthenticatorId](vdi.entity.RADIUSAuthenticatorId.md)|  The ID of the RADIUS authenticator to delete.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityInUse](vdi.fault.EntityInUse.md)| Thrown if the RADIUS authentication is currently being used by a connection server.  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_RADIUS_AUTHENTICATOR_DELETED|  If the RADIUS authenticator was successfully deleted.   
VLSI_RADIUS_AUTHENTICATOR_DELETE_FAILED|  If the RADIUS authenticator could not be deleted.   
  
Show WSDL type definition

  
  
  



Retrieves information about a RADIUS authenticator. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view is required to retrieve information about a RADIUS authenticator.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RADIUSAuthenticator](vdi.infrastructure.RADIUSAuthenticator.md) used to make the method call.   
**id**| [RADIUSAuthenticatorId](vdi.entity.RADIUSAuthenticatorId.md)|  The ID of the RADIUS authenticator.   
  
  


Return Value 

Type |  Description   
---|---  
[RADIUSAuthenticatorInfo](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorInfo.md)| Information about the specified RADIUS authenticator.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Lists the configured RADIUS authenticators. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view is required to list RADIUS authenticators.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RADIUSAuthenticator](vdi.infrastructure.RADIUSAuthenticator.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[RADIUSAuthenticatorInfo[]](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorInfo.md)| Information about the configured RADIUS authenticators.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Updates a RADIUS authenticator. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update a RADIUS authenticator.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RADIUSAuthenticator](vdi.infrastructure.RADIUSAuthenticator.md) used to make the method call.   
**id**| [RADIUSAuthenticatorId](vdi.entity.RADIUSAuthenticatorId.md)|  The ID of the RADIUS authenticator to update.   
  
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  Key value pairs describing attributes to be updated.   


  * This parameter is an update map based on [RADIUSAuthenticatorInfo](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorInfo.md "RADIUSAuthenticatorInfo"). 

  
  


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
VLSI_RADIUS_AUTHENTICATOR_UPDATED|  If the RADIUS authenticator was successfully updated.   
VLSI_RADIUS_AUTHENTICATOR_UPDATE_FAILED|  If the RADIUS authenticator could not be updated.   
  
Show WSDL type definition

  
  
  
  
  
  
  

