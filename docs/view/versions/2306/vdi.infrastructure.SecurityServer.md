---
layout: page
title: Service - SecurityServer
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.SecurityServer`

See also
> [MapEntry](vdi.util.MapEntry.md), [SecurityServerId](vdi.entity.SecurityServerId.md), [SecurityServerInfo](vdi.infrastructure.SecurityServer.SecurityServerInfo.md)

Since
> Horizon View 6.0





## Service Description

**Deprecated.**_This service is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._

Service interface for View Security Server Edit.

Methods

Methods defined in this Service
---
SecurityServer_Get, SecurityServer_List, SecurityServer_Update




**Deprecated.**_This API is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._

Get the SecurityServerInfo.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to retrieve information about a Connection Server.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SecurityServer](vdi.infrastructure.SecurityServer.md) used to make the method call.
**id**| [SecurityServerId](vdi.entity.SecurityServerId.md)|  The Id of the Security Server.




Return Value

Type |  Description
---|---
[SecurityServerInfo](vdi.infrastructure.SecurityServer.SecurityServerInfo.md)| Description of a Security Server.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._

Get the SecurityServerInfo objects of all the security servers.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to retrieve information about a Security Server.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SecurityServer](vdi.infrastructure.SecurityServer.md) used to make the method call.



Return Value

Type |  Description
---|---
[SecurityServerInfo[]](vdi.infrastructure.SecurityServer.SecurityServerInfo.md)| List of all SecurityServerInfo objects.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._

Update SecurityServer configuration with the set of attributes in the map.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management privilege is required to update Security Server information.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SecurityServer](vdi.infrastructure.SecurityServer.md) used to make the method call.
**id**| [SecurityServerId](vdi.entity.SecurityServerId.md)|  The Id of the Security Server.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  Key value pairs describing attributes to be updated. [^302]





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
ADMIN_SECURITY_SERVER_EDITED|  Fired once for each attribute changed in the connection broker
ADMIN_SECURITY_SERVER_EDIT_FAILED|  Fired if the update failed.

Show WSDL type definition












 
