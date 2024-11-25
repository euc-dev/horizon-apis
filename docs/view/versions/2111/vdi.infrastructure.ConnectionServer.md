---
layout: page
title: Service - ConnectionServer
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer`

See also
> [ConnectionServerId](vdi.entity.ConnectionServerId.md), [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon View 6.0





## Service Description

Service interface for View Server Edit.

**Methods**

Methods defined in this Service:
ConnectionServer_BackupNow, ConnectionServer_Get, ConnectionServer_GetKnownDomains, ConnectionServer_GetTags, ConnectionServer_List, ConnectionServer_Update




Provides the ability to trigger backup immediately on a given ConnectionServer of the POD.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management privilege is required to initiate Ldap backup.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ConnectionServer](vdi.infrastructure.ConnectionServer.md) used to make the method call.
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The Id of the Connection Server.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_CONNECTION_SERVER_BACKUP_INITIATED|  Fired once connection server backup is initiated.
VLSI_CONNECTION_SERVER_BACKUP_FAILED|  Fired if the backup initiation fails.

Show WSDL type definition







Get the ConnectionServerInfo.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to retrieve information about a Connection Server.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ConnectionServer](vdi.infrastructure.ConnectionServer.md) used to make the method call.
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The Id of the Connection Server.




**Return Value**

Type | Description
:---|:---
[ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md)| Description of a Connection Server.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Returns the known Active Directory domains for the connection server.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to retrieve information about a Connection Server.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ConnectionServer](vdi.infrastructure.ConnectionServer.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
xsd:string[]| Array of all the known Active Directory domain DNS names.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Returns the tags of all connection servers of the POD. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  privilege is required to get the list of Connection server tags.
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of Connection server tags.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ConnectionServer](vdi.infrastructure.ConnectionServer.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
xsd:string[]| An Array containing the tags on all connection servers.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get the ConnectionServerInfo objects of all the connection servers.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to retrieve information about a Connection Server.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ConnectionServer](vdi.infrastructure.ConnectionServer.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[ConnectionServerInfo[]](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md)| List of all ConnectionServerInfo objects.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Update ConnectionServer configuration with the set of attributes in the map.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management privilege is required to update Connection Server information.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ConnectionServer](vdi.infrastructure.ConnectionServer.md) used to make the method call.
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The Id of the Connection Server.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  Key value pairs describing attributes to be updated. [^249]





**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
ADMIN_CONNECTION_BROKER_UPDATED|  Fired once for each attribute changed in the connection broker
ADMIN_CONNECTION_BROKER_UPDATE_FAILED|  Fired if the update failed.

Show WSDL type definition












 


[^249]: This parameter is an update map based on [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md "ConnectionServerInfo").