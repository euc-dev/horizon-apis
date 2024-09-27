---
layout: page
title: Service - GatewayAccessUserOrGroup
hide:
 #- navigation
 - toc
---

  
   
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.GatewayAccessUserOrGroup  
See also
     [GatewayAccessUserOrGroupData](vdi.users.GatewayAccessUserOrGroup.GatewayAccessUserOrGroupData.md), [GatewayAccessUserOrGroupInfo](vdi.users.GatewayAccessUserOrGroup.GatewayAccessUserOrGroupInfo.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon 7.4

  


## Service Description

Interface for Gateway Access user or group. 

Methods

Methods defined in this Service   
---  
GatewayAccessUserOrGroup_Create, GatewayAccessUserOrGroup_Delete, GatewayAccessUserOrGroup_Get, GatewayAccessUserOrGroup_List  
  



Creates Gateway Access user or group using user or group data. Only [sid](vdi.users.GatewayAccessUserOrGroup.GatewayAccessUserOrGroupData.md#sid) field is required/used for creating Gateway Access user or group. All other fields will be ignored/unused during create operation. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  is required to create Gateway Access user/group.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GatewayAccessUserOrGroup](vdi.users.GatewayAccessUserOrGroup.md) used to make the method call.   
**data**| [GatewayAccessUserOrGroupData](vdi.users.GatewayAccessUserOrGroup.GatewayAccessUserOrGroupData.md)|  attributes needed to create a Gateway Access user or group.   
  
  


Return Value 

Type |  Description   
---|---  
[UserOrGroupId](vdi.entity.UserOrGroupId.md)|   
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if user or group is already an Gateway Access user or group.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_GATEWAY_ACCESS_USER_GROUP_CREATED|  If the Gateway Access user or group was successfully created.   
VLSI_GATEWAY_ACCESS_USER_GROUP_CREATE_FAILED|  If the Gateway Access user or group could not be created.   
  
Show WSDL type definition

  
  
  



Deletes Gateway Access user or group entry. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  is required to delete Gateway Access user/group.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GatewayAccessUserOrGroup](vdi.users.GatewayAccessUserOrGroup.md) used to make the method call.   
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User id of Gateway Access user or group.   
  
  


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
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if user or group is not an Gateway Access user or group.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_GATEWAY_ACCESS_USER_GROUP_DELETED|  If the Gateway Access user or group was successfully deleted.   
VLSI_GATEWAY_ACCESS_USER_GROUP_DELETE_FAILED|  If the Gateway Access user or group could not be deleted.   
  
Show WSDL type definition

  
  
  



Gets Gateway Access user info using id. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global config view privilege is required to read a Gateway Access user or group info.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GatewayAccessUserOrGroup](vdi.users.GatewayAccessUserOrGroup.md) used to make the method call.   
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User id of Gateway Access user or group.   
  
  


Return Value 

Type |  Description   
---|---  
[GatewayAccessUserOrGroupInfo](vdi.users.GatewayAccessUserOrGroup.GatewayAccessUserOrGroupInfo.md)| GatewayAccessUserOrGroupInfo for the user or group with the given user or group id.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Lists all Gateway Access users and groups. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global config view privilege is required to list the Gateway Access users or groups information.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GatewayAccessUserOrGroup](vdi.users.GatewayAccessUserOrGroup.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[GatewayAccessUserOrGroupInfo[]](vdi.users.GatewayAccessUserOrGroup.GatewayAccessUserOrGroupInfo.md)| The list of all the Gateway Access users/groups info.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  

