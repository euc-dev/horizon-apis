---
layout: page
title: Service - SecondaryCredentials
hide:
 #- navigation
 - toc
---

  
 
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.SecondaryCredentials`

See also  
> [MapEntry](vdi.util.MapEntry.md), [SecondaryCredentialsDeleteSpec](vdi.users.SecondaryCredentials.DeleteSpec.md), [SecondaryCredentialsId](vdi.entity.SecondaryCredentialsId.md), [SecondaryCredentialsInfo](vdi.users.SecondaryCredentials.SecondaryCredentialsInfo.md), [SecondaryCredentialsSpec](vdi.users.SecondaryCredentials.SecondaryCredentialsSpec.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since  
> Horizon 7.7


  


## Service Description

Service Interface for SecondaryCredentials Setting. 

Methods

Methods defined in this Service   
---  
SecondaryCredentials_Create, SecondaryCredentials_Delete, SecondaryCredentials_Get, SecondaryCredentials_List, SecondaryCredentials_Update  
  



Create a new Secondary Credentials Setting. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management privilege is required to create Secondary Credentials.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SecondaryCredentials](vdi.users.SecondaryCredentials.md) used to make the method call.   
**spec**| [SecondaryCredentialsSpec](vdi.users.SecondaryCredentials.SecondaryCredentialsSpec.md)|  The Secondary Credentials Spec   
  
  


Return Value 

Type |  Description   
---|---  
[SecondaryCredentialsId](vdi.entity.SecondaryCredentialsId.md)| id  
  


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
VLSI_SECONDARY_CREDENTIALS_CREATED|  if Secondary Credentials creation succeeds.   
VLSI_SECONDARY_CREDENTIALS_CREATE_FAILED|  if Secondary Credentials creation fails.   
  
Show WSDL type definition

  
  
  



Delete a given SecondaryCredentials Setting. Either of id or spec needs to be provided. If id and spec both are provided then delete happens as per id. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management privilege is required to delete Secondary Credentials.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SecondaryCredentials](vdi.users.SecondaryCredentials.md) used to make the method call.   
**id**| [SecondaryCredentialsId](vdi.entity.SecondaryCredentialsId.md)|  The entityId of the SecondaryCredentials to be deleted.   


  * This parameter need not be set.

  
**spec**| [SecondaryCredentialsDeleteSpec](vdi.users.SecondaryCredentials.DeleteSpec.md)|  The specification for deleting the SecondaryCredentials.   


  * This parameter need not be set.

  
  


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
VLSI_SECONDARY_CREDENTIALS_DELETED|  if the SecondaryCredentials is successfully deleted.   
VLSI_SECONDARY_CREDENTIALS_DELETE_FAILED|  if the SecondaryCredentials deletion failed.   
  
Show WSDL type definition

  
  
  



Get a SecondaryCredentials Setting by Id. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to get Secondary Credentials.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SecondaryCredentials](vdi.users.SecondaryCredentials.md) used to make the method call.   
**id**| [SecondaryCredentialsId](vdi.entity.SecondaryCredentialsId.md)|  The entityId of the Secondary Credentials to get.   
  
  


Return Value 

Type |  Description   
---|---  
[SecondaryCredentialsInfo](vdi.users.SecondaryCredentials.SecondaryCredentialsInfo.md)| requested SecondaryCredentialsInfo entity  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



List the configured Secondary Credentials for given user. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to list Secondary Credentials.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SecondaryCredentials](vdi.users.SecondaryCredentials.md) used to make the method call.   
**ownerId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The UserOrGroupId of the owner.   
  
  


Return Value 

Type |  Description   
---|---  
[SecondaryCredentialsInfo[]](vdi.users.SecondaryCredentials.SecondaryCredentialsInfo.md)| requested array of SecondaryCredentialsInfo entity.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Update the SecondaryCredentials with the set of attributes in the map. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management privilege is required to update Secondary Credentials.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SecondaryCredentials](vdi.users.SecondaryCredentials.md) used to make the method call.   
**id**| [SecondaryCredentialsId](vdi.entity.SecondaryCredentialsId.md)|  The entityId of the SecondaryCredentials to be updated.   
  
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  The key-value pairs describing attributes to be updated.   


  * This parameter is an update map based on [SecondaryCredentialsInfo](vdi.users.SecondaryCredentials.SecondaryCredentialsInfo.md "SecondaryCredentialsInfo"). 

  
  


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
VLSI_SECONDARY_CREDENTIALS_UPDATED|  for each SecondaryCredentials attribute that was updated.   
VLSI_SECONDARY_CREDENTIALS_UPDATE_FAILED|  if SecondaryCredentials update failed.   
  
Show WSDL type definition

  
  
  
  
  
  
  
