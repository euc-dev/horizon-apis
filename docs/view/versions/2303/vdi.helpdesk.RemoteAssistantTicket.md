---
layout: page
title: Service - RemoteAssistantTicket
hide:
#  - navigation
  - toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.RemoteAssistantTicket`

See also
> [RemoteAssistantTicketInfo](vdi.helpdesk.RemoteAssistantTicket.RemoteAssistantTicketInfo.md), [SessionId](vdi.entity.SessionId.md)

Since
> Horizon 7.2





## Service Description

The service for fetching Microsoft Remote Assistant ticket.

**Methods**

Methods defined in this Service:
RemoteAssistantTicket_Get




Get a Microsoft Remote Assistance ticket by session Id.

**Privileges**

Privilege | Description
:---|:---
REMOTE_ASSISTANCE|  privilege is required to get a Microsoft Remote Assistant ticket.
MACHINE_MANAGEMENT|  is sufficient to get Microsoft Remote Assistant ticket.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RemoteAssistantTicket](vdi.helpdesk.RemoteAssistantTicket.md) used to make the method call.
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionID to get a Microsoft Remote Assistance ticket for.




**Return Value**

Type | Description
:---|:---
[RemoteAssistantTicketInfo](vdi.helpdesk.RemoteAssistantTicket.RemoteAssistantTicketInfo.md)| The Microsoft Remote Assistant ticket



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
ADMIN_SESSION_REMOTE_ASSISTANT_TICKET|  For local sessions, if a Microsoft Remote Assistant ticket is successfully obtained.
ADMIN_SESSION_REMOTE_ASSISTANT_TICKET_FAILED|  For local sessions, if unable to obtain a Microsoft Remote Assistant ticket.
VLSI_FEDERATED_DESKTOP_SESSION_REMOTE_ASSISTANT_TICKET_REQUEST_SENT|  For remote sessions, if a request was successfully made to obtain a Microsoft Remote Assistant ticket.
VLSI_FEDERATED_DESKTOP_SESSION_REMOTE_ASSISTANT_TICKET_REQUEST_SEND_FAILED|  For remote sessions, if a request could not be made to obtain a Microsoft Remote Assistant ticket.

Show WSDL type definition












 
