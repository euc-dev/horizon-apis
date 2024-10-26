---
layout: page
title: Service - RDSServer
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer`

See also
> [MapEntry](vdi.util.MapEntry.md), [RDSServerId](vdi.entity.RDSServerId.md), [RDSServerInfo](vdi.resources.RDSServer.RDSServerInfo.md), [RDSServerRegisterResult](vdi.resources.RDSServer.RegisterResult.md), [RDSServerRegisterSpec](vdi.resources.RDSServer.RegisterSpec.md), [RDSServerSummaryView](vdi.resources.RDSServer.RDSServerSummaryView.md)

Since
> Horizon View 6.0





## Service Description

Interface representing an RDS server

Methods

Methods defined in this Service
---
RDSServer_Delete, RDSServer_Get, RDSServer_GetSummaryView, RDSServer_Recover, RDSServer_RecoverMachines, RDSServer_Register, RDSServer_Update




Remove a given RDSServer from the View LDAP configuration.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  privilege is required to delete RDS Server.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RDSServer](vdi.resources.RDSServer.md) used to make the method call.
**id**| [RDSServerId](vdi.entity.RDSServerId.md)|  The entityId of RDSServer to delete




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
VLSI_RDSSERVER_DELETED|  if the RDSServer is successfully deleted.
VLSI_RDSSERVER_DELETE_FAILED|  if the RDSServer deletion failed.

Show WSDL type definition







Get an RDSServer by Id. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  is required to get an RDSServer that is not in-use. It is sufficient to get all RDSServers that may or may not be associated with a Farm.
POOL_VIEW|  is required to get RDSServer that is associated with a Farm. All in-use RDSServers can be accessed with POOL_VIEW on the Root access group. With POOL_VIEW privilege on a non-Root Farm access group, only the RDSServers associated with the Farm can be accessed.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RDSServer](vdi.resources.RDSServer.md) used to make the method call.
**id**| [RDSServerId](vdi.entity.RDSServerId.md)|  The entityId of RDSServer to get




Return Value

Type |  Description
---|---
[RDSServerInfo](vdi.resources.RDSServer.RDSServerInfo.md)| requested RDSServer entity



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get an RDSServerSummaryView by Id. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  is required to get an RDSServer that is not in-use. It is sufficient to get all RDSServers that may or may not be associated with a Farm.
POOL_VIEW|  is required to get RDSServer that is associated with a Farm. All in-use RDSServers can be accessed with POOL_VIEW on the Root access group. With POOL_VIEW privilege on a non-Root Farm access group, only the RDSServers associated with the Farm can be accessed.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RDSServer](vdi.resources.RDSServer.md) used to make the method call.
**id**| [RDSServerId](vdi.entity.RDSServerId.md)|  The entityId of RDSServer to get




Return Value

Type |  Description
---|---
[RDSServerSummaryView](vdi.resources.RDSServer.RDSServerSummaryView.md)| requested RDSServer entity



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Mark the RDS server for recovery. This operation deletes the current RDS server and provisions a new RDS server from latest image. Usually this operation is used to recover RDS server that is in error state or otherwise unusable. This operation applies only to RDS server belonging to Instant Clone Engine farms. Requires at least one of the listed privileges.
Note :- The RDS server being recovered must not have any active user session, otherwise this operation would fail.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  privilege is required to recover the RDS server.
POOL_MANAGEMENT|  privilege is required to recover the RDS server.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RDSServer](vdi.resources.RDSServer.md) used to make the method call.
**id**| [RDSServerId](vdi.entity.RDSServerId.md)|  Unique identifier of the RDS server to recover. RDSServerId of this type must originate from the [RDSServer](vdi.resources.RDSServer.md) service.




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
VLSI_RDSSERVER_RECOVERY_REQUESTED|  if RDS server was marked for recovery.
VLSI_RDSSERVER_RECOVERY_REQUEST_FAILED|  if failed to mark the RDS server for recovery.

Show WSDL type definition







Mark the RDS servers for recovery. This operation deletes the current RDS servers and provisions new RDS servers from latest image. Usually this operation is used to recover RDS servers that are in error state or otherwise unusable. This operation applies only to RDS servers belonging to Instant Clone Engine farms. Requires at least one of the listed privileges.
Note :- The RDS servers being recovered must not have any active user session, otherwise this operation would fail.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  privilege is required to recover the RDS servers.
POOL_MANAGEMENT|  privilege is required to recover the RDS servers.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RDSServer](vdi.resources.RDSServer.md) used to make the method call.
**ids**| [RDSServerId[]](vdi.entity.RDSServerId.md)|  Array of unique identifiers of the RDS servers to recover. RDSServerIds of this type must originate from the [RDSServer](vdi.resources.RDSServer.md) service.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if recover operation fails on one or more RDS servers.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_RDSSERVER_RECOVERY_REQUESTED|  if RDS servers were marked for recovery.
VLSI_RDSSERVER_RECOVERY_REQUEST_FAILED|  if failed to mark the RDS servers for recovery.

Show WSDL type definition







Registers an RDS server.

Privileges

Privilege |  Description
---|---
GLOBAL_MACHINE_REGISTER|  Global machine registration privilege is required to register an RDS Server.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RDSServer](vdi.resources.RDSServer.md) used to make the method call.
**spec**| [RDSServerRegisterSpec](vdi.resources.RDSServer.RegisterSpec.md)|  The specification for the register operation.




Return Value

Type |  Description
---|---
[RDSServerRegisterResult](vdi.resources.RDSServer.RegisterResult.md)| The registration result.



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
VLSI_RDSSERVER_REGISTERED|  If the RDS Server is successfully registered.
VLSI_RDSSERVER_REGISTRATION_FAILED|  If the RDS Server could not be registered.

Show WSDL type definition







Update an RDS server with the set of attributes in the map. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  privilege is required to update RDS Server configuration.
POOL_MANAGEMENT|  privilege is sufficient when [enabled](vdi.resources.RDSServer.RDSServerSettings.md#enabled) alone is being updated.
MACHINE_MANAGEMENT|  privilege is sufficient when [enabled](vdi.resources.RDSServer.RDSServerSettings.md#enabled) alone is being updated.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RDSServer](vdi.resources.RDSServer.md) used to make the method call.
**id**| [RDSServerId](vdi.entity.RDSServerId.md)|  The entity Id of the RDS server to be updated
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  The key-value pairs describing attributes to be updated [^198]





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
VLSI_RDSSERVER_UPDATED|  for each RDSServer attribute that was updated.
VLSI_RDSSERVER_UPDATE_FAILED|  if the RDSServer update failed.

Show WSDL type definition












 


[^198]: This parameter is an update map based on [RDSServerInfo](vdi.resources.RDSServer.RDSServerInfo.md "RDSServerInfo").