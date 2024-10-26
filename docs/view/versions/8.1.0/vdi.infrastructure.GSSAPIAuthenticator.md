---
layout: page
title: Service - GSSAPIAuthenticator
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.GSSAPIAuthenticator`

See also
> [GSSAPIAuthenticatorId](vdi.entity.GSSAPIAuthenticatorId.md), [GSSAPIAuthenticatorInfo](vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorInfo.md), [GSSAPIAuthenticatorSpec](vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorSpec.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon 7.13





## Service Description

Service for managing GSSAPI authenticators.

Methods

Methods defined in this Service
---
GSSAPIAuthenticator_Create, GSSAPIAuthenticator_Delete, GSSAPIAuthenticator_Get, GSSAPIAuthenticator_List, GSSAPIAuthenticator_Update




Creates a GSSAPI authenticator.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to create a GSSAPI authenticator.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GSSAPIAuthenticator](vdi.infrastructure.GSSAPIAuthenticator.md) used to make the method call.
**spec**| [GSSAPIAuthenticatorSpec](vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorSpec.md)|  The specification of the GSSAPI authenticator.




Return Value

Type |  Description
---|---
[GSSAPIAuthenticatorId](vdi.entity.GSSAPIAuthenticatorId.md)| The ID of the newly created GSSAPI authenticator.



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
GSSAPI_AUTHENTICATOR_CREATED|  If the GSSAPI authenticator was successfully created.

Show WSDL type definition







Deletes the specified GSSAPI authenticator.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete a GSSAPI authenticator.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GSSAPIAuthenticator](vdi.infrastructure.GSSAPIAuthenticator.md) used to make the method call.
**id**| [GSSAPIAuthenticatorId](vdi.entity.GSSAPIAuthenticatorId.md)|  The ID of the GSSAPI authenticator to delete.




Return Value

Type |  Description
---|---
None



Faults

Type |  Description
---|---
[EntityInUse](vdi.fault.EntityInUse.md)| Thrown if the GSSAPI authentication is currently being used by a connection server.
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
GSSAPI_AUTHENTICATOR_DELETED|  If the GSSAPI authenticator was successfully deleted.

Show WSDL type definition







Retrieves information about a GSSAPI authenticator.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to retrieve information about a GSSAPI authenticator.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GSSAPIAuthenticator](vdi.infrastructure.GSSAPIAuthenticator.md) used to make the method call.
**id**| [GSSAPIAuthenticatorId](vdi.entity.GSSAPIAuthenticatorId.md)|  The ID of the GSSAPI authenticator.




Return Value

Type |  Description
---|---
[GSSAPIAuthenticatorInfo](vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorInfo.md)| Information about the specified GSSAPI authenticator.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Lists the configured GSSAPI authenticators.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to list GSSAPI authenticators.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GSSAPIAuthenticator](vdi.infrastructure.GSSAPIAuthenticator.md) used to make the method call.



Return Value

Type |  Description
---|---
[GSSAPIAuthenticatorInfo[]](vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorInfo.md)| Information about the configured GSSAPI authenticators.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Updates a GSSAPI authenticator.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update a GSSAPI authenticator.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GSSAPIAuthenticator](vdi.infrastructure.GSSAPIAuthenticator.md) used to make the method call.
**id**| [GSSAPIAuthenticatorId](vdi.entity.GSSAPIAuthenticatorId.md)|  The ID of the GSSAPI authenticator to update.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  Key value pairs describing attributes to be updated. [^291]





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
GSSAPI_AUTHENTICATOR_UPDATED|  If the GSSAPI authenticator was successfully updated.

Show WSDL type definition












 


[^291]: This parameter is an update map based on [GSSAPIAuthenticatorInfo](vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorInfo.md "GSSAPIAuthenticatorInfo").