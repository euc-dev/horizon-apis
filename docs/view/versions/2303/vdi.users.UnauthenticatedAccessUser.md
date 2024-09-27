---
layout: page
title: Service - UnauthenticatedAccessUser
hide:
 #- navigation
 - toc
---

  
  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.UnauthenticatedAccessUser  
See also
     [UnauthenticatedAccessUserData](vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserData.md), [UnauthenticatedAccessUserInfo](vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserInfo.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon 7.1

  


## Service Description

Service Interface for Unauthenticated Access user settings. 

Methods

Methods defined in this Service   
---  
UnauthenticatedAccessUser_Create, UnauthenticatedAccessUser_Delete, UnauthenticatedAccessUser_Get, UnauthenticatedAccessUser_IsUnauthenticatedAccessUser, UnauthenticatedAccessUser_List, UnauthenticatedAccessUser_Update  
  



Creates Unauthenticated Access user using user data. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global management is required to create a new Unauthenticated Access user.   
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to to create a new Unauthenticated Access user.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UnauthenticatedAccessUser](vdi.users.UnauthenticatedAccessUser.md) used to make the method call.   
**userData**| [UnauthenticatedAccessUserData](vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserData.md)|  attributes needed to create a Unauthenticated Access user.   
  
  


Return Value 

Type |  Description   
---|---  
[UserOrGroupId](vdi.entity.UserOrGroupId.md)| User Id used for creating Unauthenticated Access user.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if user is already an Unauthenticated Access user. Thrown if user is a kiosk user. Thrown if User Principal Name is null or empty.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_UNAUTHENTICATED_ACCESS_USER_CREATED|  If the Unauthenticated Access user was successfully created.   
VLSI_UNAUTHENTICATED_ACCESS_USER_CREATION_FAILED|  If the Unauthenticated Access user could not be created.   
  
Show WSDL type definition

  
  
  



Deletes Unauthenticated Access user entry. Note that only users which was created in current pod can be deleted. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  is required to delete Unauthenticated Access user.   
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to delete Unauthenticated Access user.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UnauthenticatedAccessUser](vdi.users.UnauthenticatedAccessUser.md) used to make the method call.   
**userId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  AD user id which Unauthenticated Access user is associated with.   
  
  


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
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if user is not an Unauthenticated Access user. Thrown if Unauthenticated Access user was created by other pod.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_UNAUTHENTICATED_ACCESS_USER_DELETED|  If the Unauthenticated Access user was successfully deleted.   
VLSI_UNAUTHENTICATED_ACCESS_USER_DELETION_FAILED|  If the Unauthenticated Access user could not be deleted.   
  
Show WSDL type definition

  
  
  



Gets Unauthenticated Access user info using id. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global config view privilege is required to read a Unauthenticated Access user info.   
FEDERATED_LDAP_VIEW|  Global LDAP view is required to read a global Unauthenticated Access user info.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UnauthenticatedAccessUser](vdi.users.UnauthenticatedAccessUser.md) used to make the method call.   
**userId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User id of AD user.   
  
  


Return Value 

Type |  Description   
---|---  
[UnauthenticatedAccessUserInfo](vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserInfo.md)| Unauthenticated Access user info for the user with the given userId.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Returns true if the unauthenticated access user exists with given userId. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UnauthenticatedAccessUser](vdi.users.UnauthenticatedAccessUser.md) used to make the method call.   
**userId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  AD user id which Unauthenticated Access user is associated with.   
  
  


Return Value 

Type |  Description   
---|---  
xsd:boolean| Returns true if the unauthenticated access user exists with given userId.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Lists the Unauthenticated Access User info of all Unauthenticated Access users. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global config view privilege is required to list the Unauthenticated Access users information.   
FEDERATED_LDAP_VIEW|  Global LDAP view is required to list global Unauthenticated Access users information.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UnauthenticatedAccessUser](vdi.users.UnauthenticatedAccessUser.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[UnauthenticatedAccessUserInfo[]](vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserInfo.md)| The list of all the Unauthenticated Access users info.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Updates Unauthenticated Access user using user data. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global management is required to update existing Unauthenticated Access user.   
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to to update existing Unauthenticated Access user.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UnauthenticatedAccessUser](vdi.users.UnauthenticatedAccessUser.md) used to make the method call.   
**userData**| [UnauthenticatedAccessUserData](vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserData.md)|  attributes needed to create a Unauthenticated Access user.   
  
  


Return Value 

Type |  Description   
---|---  
[UserOrGroupId](vdi.entity.UserOrGroupId.md)| User Id used for creating Unauthenticated Access user.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if user is not member of local pod. Thrown if user is a kiosk user. Thrown if User Principal Name is null or empty.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_UNAUTHENTICATED_ACCESS_USER_UPDATED|  If the Unauthenticated Access user was successfully updated.   
VLSI_UNAUTHENTICATED_ACCESS_USER_UPDATE_FAILED|  If the Unauthenticated Access user could not be updated.   
  
Show WSDL type definition

  
  
  
  
  
  
  

