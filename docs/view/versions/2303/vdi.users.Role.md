---
layout: page
title: Service - Role
hide:
 #- navigation
 - toc
---

  
  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.Role  
See also
     [MapEntry](vdi.util.MapEntry.md), [RoleBase](vdi.users.Role.RoleBase.md), [RoleId](vdi.entity.RoleId.md), [RoleInfo](vdi.users.Role.RoleInfo.md)  
Since 
    Horizon View 6.0

  


## Service Description

Information about a role. This represents a name and description tied to a set of admin privileges. Privileges represents certain actions allowed by an admin on various resources. Roles may either be system defined (builtin) or admin created (custom). Different sets of privileges may be defined depending on the role type. Only custom roles may be edited. 

Methods

Methods defined in this Service   
---  
Role_Create, Role_Delete, Role_Get, Role_List, Role_Update  
  



Add a new custom role. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_ROLE_MANAGEMENT|  Role management privilege is required to create a role.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Role](vdi.users.Role.md) used to make the method call.   
**base**| [RoleBase](vdi.users.Role.RoleBase.md)|  attributes needed to add a role   
  
  


Return Value 

Type |  Description   
---|---  
[RoleId](vdi.entity.RoleId.md)| unique identifier  
  


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
ADMIN_ROLE_ADDED|  Sent when a role is successfully created.   
ADMIN_ROLE_ADD_FAILED|  Sent when a role fails to be created.   
  
Show WSDL type definition

  
  
  



Delete a given role and all permissions associated with it. This is only allowed for custom roles. Attempting to delete a builtin role will result in an InvalidRequest exception. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_ROLE_MANAGEMENT|  Role management privilege is necessary to delete a role.   
GLOBAL_PERMISSION_VIEW|  Permission read access privilege is necessary to delete a role.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Role](vdi.users.Role.md) used to make the method call.   
**id**| [RoleId](vdi.entity.RoleId.md)|  RoleId of entity to delete.   
  
  


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
ADMIN_ROLE_REMOVED|  Sent when a role is successfully deleted.   
ADMIN_ROLE_REMOVE_FAILED|  Sent when a role fails to be deleted.   
  
Show WSDL type definition

  
  
  



Get an role by Id. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_ROLE_VIEW|  Role read access privilege is required to read a role.   
GLOBAL_PERMISSION_VIEW|  Permission read access privilege is required to include any permission information in a role.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Role](vdi.users.Role.md) used to make the method call.   
**id**| [RoleId](vdi.entity.RoleId.md)|  RoleId of entity to get.   
  
  


Return Value 

Type |  Description   
---|---  
[RoleInfo](vdi.users.Role.RoleInfo.md)| requested role entity.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Lists all the roles. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_ROLE_VIEW|  Role read access privilege is required to read all role.   
GLOBAL_PERMISSION_VIEW|  Permission read access privilege is required to include any permission information in any roles.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Role](vdi.users.Role.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[RoleInfo[]](vdi.users.Role.RoleInfo.md)| The list of roles.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Update given role with the set of attributes in the map. This is only allowed on custom roles. Attempting to update a builtin role will result in an InvalidRequest exception. Note that certain privileges expand into selectable child privileges upon creation. These child privileges must be removed as well if the parent is removed in an update. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_ROLE_MANAGEMENT|  Role management privilege is required to update a role.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Role](vdi.users.Role.md) used to make the method call.   
**id**| [RoleId](vdi.entity.RoleId.md)|  RoleId of entity to update.   
  
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated   


  * This parameter is an update map based on [RoleInfo](vdi.users.Role.RoleInfo.md "RoleInfo"). 

  
  


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
ADMIN_ROLE_PRIV_UPDATED|  Sent when a role is successfully updated.   
ADMIN_ROLE_PRIV_UPDATE_FAILED|  Sent when a role fails to be updated.   
  
Show WSDL type definition

  
  
  
  
  
  
  

