---
layout: page
title: Service - ViewClient
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.ViewClient`

See also
> [SessionId](vdi.entity.SessionId.md), [ViewClientInfo](vdi.helpdesk.ViewClient.ViewClientInfo.md)

Since
> Horizon 7.2





## Service Description

The service for fetching View client and endpoint machine information.

Methods

Methods defined in this Service
---
ViewClient_Get




Retrieves View client and the endpoint machine information of the session.

Privileges

Privilege |  Description
---|---
MACHINE_VIEW|  Machine read with the corresponding access group permission is sufficient to get a session's client information.
POOL_VIEW|  Desktop read with the corresponding access group permission is sufficient to get a session's client information.
FEDERATED_SESSIONS_VIEW|  Global session read is sufficient to get a session's client information.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewClient](vdi.helpdesk.ViewClient.md) used to make the method call.
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionID to get the client information for.




Return Value

Type |  Description
---|---
[ViewClientInfo](vdi.helpdesk.ViewClient.ViewClientInfo.md)| Client information of the session.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
