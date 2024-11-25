---
layout: page
title: Service - RemoteApplication
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.helpdesk.RemoteApplication`

See also
> [SessionId](vdi.entity.SessionId.md)

Since
> Horizon 7.4





## Service Description

The service for fetching remote application information.

**Methods**

Methods defined in this Service:
RemoteApplication_EndApplication, RemoteApplication_GetS4BPairingMode




Terminate an application running on virtual machine by session Id and the application Id.

**Privileges**

Privilege | Description
:---|:---
MANAGE_REMOTE_PROCESS|  Remote process management with the corresponding access group permission is required to terminate a remote application.
MACHINE_MANAGEMENT|  Desktop management with the corresponding access group permission is sufficient to terminate a remote application.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RemoteApplication](vdi.helpdesk.RemoteApplication.md) used to make the method call.
**id**| [SessionId](vdi.entity.SessionId.md)|  ID of the session which contains the application to be terminated.
**applicationId**|  xsd:string|  ID of a remote application.




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

Show WSDL type definition







Retrieves the Skype for Business (S4B) pairing mode from endpoint machine by session Id.

**Privileges**

Privilege | Description
:---|:---
MACHINE_VIEW|  Machine read with the corresponding access group permission is sufficient to get a session's S4B pairing mode.
POOL_VIEW|  Desktop read with the corresponding access group permission is sufficient to get a session's S4B pairing mode.
FEDERATED_SESSIONS_VIEW|  Global session read is sufficient to get a session's S4B pairing mode.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RemoteApplication](vdi.helpdesk.RemoteApplication.md) used to make the method call.
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionID to get the S4B pair mode for.




**Return Value**

Type | Description
:---|:---
xsd:string| The Skype for Business pairing mode. The possible pairing modes are: {S4B_STATUS_OPTIMIZED, S4B_STATUS_FALLBACK, S4B_STATUS_CONNECTING, S4B_STATUS_OPTIMIZED_VERSION_MISMATCH, S4B_STATUS_FALLBACK_VERSION_MISMATCH, S4B_STATUS_CONNECTING, S4B_STATUS_DISCONNECTED, S4B_STATUS_UNDEFINED}.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
