---
layout: page
title: Service - Session
hide:
 #- navigation
 - toc
---

  
   
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.Session`

See also  
> [SessionId](vdi.entity.SessionId.md), [SessionLocalSummaryView](vdi.users.Session.SessionLocalSummaryView.md)

Since  
> Horizon View 6.0


  


## Service Description

The interface for sessions. 

Methods

Methods defined in this Service   
---  
Session_Disconnect, Session_DisconnectSessions, Session_GetLocalSummaryView, Session_Logoff, Session_LogoffForced, Session_LogoffSessions, Session_LogoffSessionsForced, Session_Reset, Session_ResetSessions, Session_Restart, Session_RestartSessions, Session_SendMessage, Session_SendMessages  
  



Disconnects a session. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_MANAGE_VDI_SESSION|  Machine session management with the corresponding access group permission is sufficient to disconnect a session.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to disconnect a session.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  unique identifier for session   
  
  


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
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the session is already disconnected  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_DESKTOP_SESSION_DISCONNECTED|  For local sessions, if the session was successfully disconnected.   
ADMIN_DESKTOP_SESSION_DISCONNECT_FAILED|  For local sessions, if the session could not be disconnected.   
VLSI_FEDERATED_DESKTOP_SESSION_DISCONNECT_REQUEST_SENT|  For remote sessions, if a request was successfully made to disconnect the session.   
VLSI_FEDERATED_DESKTOP_SESSION_DISCONNECT_REQUEST_SEND_FAILED|  For remote sessions, if a request could not be made to disconnect the session.   
  
Show WSDL type definition

  
  
  



Disconnects multiple sessions. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_MANAGE_VDI_SESSION|  Machine session management with the corresponding access group permission is sufficient to disconnect a session.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to disconnect a session.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**ids**| [SessionId[]](vdi.entity.SessionId.md)|  unique identifiers for the sessions   
  
  


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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| The index of the fault will contain null on success for the corresponding index of the sessionId or an exception if an error occurred. This exception will be an EntityNotFound if the session is not found.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_DESKTOP_SESSION_DISCONNECTED|  For local sessions, sent for each session that was successfully disconnected.   
ADMIN_DESKTOP_SESSION_DISCONNECT_FAILED|  For local sessions, sent for each session that could not be disconnected.   
VLSI_FEDERATED_DESKTOP_SESSION_DISCONNECT_REQUEST_SENT|  For remote sessions, sent for each request that was successfully made to disconnect the session.   
VLSI_FEDERATED_DESKTOP_SESSION_DISCONNECT_REQUEST_SEND_FAILED|  For remote sessions, sent for each request that could not be made to disconnect the session.   
  
Show WSDL type definition

  
  
  



Get a local session's summary view. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  Machine read with the corresponding access group permission is sufficient to read a session.   
FEDERATED_SESSIONS_VIEW|  Global session read is sufficient to read a session.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionId to get the summary view for.   
  
  


Return Value 

Type |  Description   
---|---  
[SessionLocalSummaryView](vdi.users.Session.SessionLocalSummaryView.md)| Summary View for the session.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Logs off a session. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_MANAGE_VDI_SESSION|  Machine session management with the corresponding access group permission is sufficient to logoff a session.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to logoff a session.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  unique identifier for session   
  
  


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
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the session is blocked from logging off, such as from it being locked.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_DESKTOP_SESSION_LOGOFF|  For local sessions, if the session was successfully logged off.   
ADMIN_DESKTOP_SESSION_LOGOFF_FAILED|  For local sessions, if the session could not be logged off.   
VLSI_FEDERATED_DESKTOP_SESSION_LOGOFF_REQUEST_SENT|  For remote sessions, if a request was successfully made to logoff the session.   
VLSI_FEDERATED_DESKTOP_SESSION_LOGOFF_REQUEST_SEND_FAILED|  For remote sessions, if a request could not be made to logoff the session.   
  
Show WSDL type definition

  
  
  



Logs off a session forcibly. This operation will also log off a locked session. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_MANAGE_VDI_SESSION|  Machine session management with the corresponding access group permission is sufficient to logoff a session.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to logoff a session.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  unique identifier for session   
  
  


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
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the session is blocked from logging off, such as from it being locked.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_DESKTOP_SESSION_LOGOFF|  For local sessions, if the session was successfully logged off.   
ADMIN_DESKTOP_SESSION_LOGOFF_FAILED|  For local sessions, if the session could not be logged off.   
VLSI_FEDERATED_DESKTOP_SESSION_LOGOFF_REQUEST_SENT|  For remote sessions, if a request was successfully made to logoff the session.   
VLSI_FEDERATED_DESKTOP_SESSION_LOGOFF_REQUEST_SEND_FAILED|  For remote sessions, if a request could not be made to logoff the session.   
  
Show WSDL type definition

  
  
  



Logs off multiple sessions. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_MANAGE_VDI_SESSION|  Machine session management with the corresponding access group permission is sufficient to logoff a session.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to logoff a session.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**ids**| [SessionId[]](vdi.entity.SessionId.md)|  unique identifiers for the sessions   
  
  


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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| The index of the fault will contain null on success for the corresponding index of the sessionId or an exception if an error occurred. This exception will be an EntityNotFound if the session is not found.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_DESKTOP_SESSION_LOGOFF|  For local sessions, sent for each session that was successfully logged off.   
ADMIN_DESKTOP_SESSION_LOGOFF_FAILED|  For local sessions, sent for each session that could not be logged off.   
VLSI_FEDERATED_DESKTOP_SESSION_LOGOFF_REQUEST_SENT|  For remote sessions, sent for each request that was successfully made to logoff the session.   
VLSI_FEDERATED_DESKTOP_SESSION_LOGOFF_REQUEST_SEND_FAILED|  For remote sessions, sent for each request that could not be made to logoff the session.   
  
Show WSDL type definition

  
  
  



Logs off multiple sessions forcibly. This operation will also log off all the locked sessions. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_MANAGE_VDI_SESSION|  Machine session management with the corresponding access group permission is sufficient to logoff a session.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to logoff a session.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**ids**| [SessionId[]](vdi.entity.SessionId.md)|  unique identifiers for the sessions   
  
  


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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| The index of the fault will contain null on success for the corresponding index of the sessionId or an exception if an error occurred. This exception will be an EntityNotFound if the session is not found.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_DESKTOP_SESSION_LOGOFF|  For local sessions, sent for each session that was successfully logged off.   
ADMIN_DESKTOP_SESSION_LOGOFF_FAILED|  For local sessions, sent for each session that could not be logged off.   
VLSI_FEDERATED_DESKTOP_SESSION_LOGOFF_REQUEST_SENT|  For remote sessions, sent for each request that was successfully made to logoff the session.   
VLSI_FEDERATED_DESKTOP_SESSION_LOGOFF_REQUEST_SEND_FAILED|  For remote sessions, sent for each request that could not be made to logoff the session.   
  
Show WSDL type definition

  
  
  



Resets the session's machine. The machine must be managed by Virtual Center and the session cannot be an application or an RDS desktop session. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_REBOOT|  Machine reboot with the corresponding access group permission is sufficient to reset a session's machine.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to reset a session's machine.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  unique identifier for session   
  
  


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
ADMIN_DESKTOP_SESSION_REBOOTED|  For local sessions, if the session's machine was successfully reset.   
ADMIN_DESKTOP_SESSION_REBOOT_FAILED|  For local sessions, if the session's machine could not be reset.   
VLSI_FEDERATED_DESKTOP_SESSION_RESET_REQUEST_SENT|  For remote sessions, if a request was successfully made to reset the session.   
VLSI_FEDERATED_DESKTOP_SESSION_RESET_REQUEST_SEND_FAILED|  For remote sessions, if a request could not be made to reset the session.   
  
Show WSDL type definition

  
  
  



Resets multiple sessions' machines. The machines must be managed by Virtual Center and the sessions cannot be application or RDS desktop sessions. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_REBOOT|  Machine reboot with the corresponding access group permission is sufficient to reset a session's machine.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to reset a session's machine.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**ids**| [SessionId[]](vdi.entity.SessionId.md)|  unique identifiers for the sessions   
  
  


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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| The index of the fault will contain null on success for the corresponding index of the sessionId or an exception if an error occurred. This exception will be an EntityNotFound if the session is not found.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_DESKTOP_SESSION_REBOOTED|  For local sessions, sent for each session that the session's machine was successfully reset.   
ADMIN_DESKTOP_SESSION_REBOOT_FAILED|  For local sessions, sent for each session that the the session's machine could not be reset.   
VLSI_FEDERATED_DESKTOP_SESSION_RESET_REQUEST_SENT|  For remote sessions, sent for each request that was successfully made to reset the session.   
VLSI_FEDERATED_DESKTOP_SESSION_RESET_REQUEST_SEND_FAILED|  For remote sessions, sent for each request that could not be made to reset the session.   
  
Show WSDL type definition

  
  
  



Restarts the session's machine. The machine must be managed by Virtual Center and the session cannot be an application or an RDS desktop session. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_REBOOT|  Machine reboot with the corresponding access group permission is sufficient to restart a session's machine.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to restart a session's machine.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  unique identifier for session   
  
  


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
ADMIN_DESKTOP_SESSION_RESTARTED|  For local sessions, if the session's machine was successfully restarted.   
ADMIN_DESKTOP_SESSION_RESTART_FAILED|  For local sessions, if the session's machine could not be restarted.   
VLSI_FEDERATED_DESKTOP_SESSION_RESTART_REQUEST_SENT|  For remote sessions, if a request was successfully made to restart the session.   
VLSI_FEDERATED_DESKTOP_SESSION_RESTART_REQUEST_SEND_FAILED|  For remote sessions, if a request could not be made to restart the session.   
  
Show WSDL type definition

  
  
  



Restarts multiple sessions' machines. The machines must be managed by Virtual Center and the sessions cannot be application or RDS desktop sessions. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_REBOOT|  Machine reboot with the corresponding access group permission is sufficient to restart a session's machine.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to restart a session's machine.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**ids**| [SessionId[]](vdi.entity.SessionId.md)|  unique identifiers for the sessions   
  
  


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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| The index of the fault will contain null on success for the corresponding index of the sessionId or an exception if an error occurred. This exception will be an EntityNotFound if the session is not found.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_DESKTOP_SESSION_RESTARTED|  For local sessions, sent for each session that the session's machine was successfully restarted.   
ADMIN_DESKTOP_SESSION_RESTART_FAILED|  For local sessions, sent for each session that the the session's machine could not be restarted.   
VLSI_FEDERATED_DESKTOP_SESSION_RESTART_REQUEST_SENT|  For remote sessions, sent for each request that was successfully made to restart the session.   
VLSI_FEDERATED_DESKTOP_SESSION_RESTART_REQUEST_SEND_FAILED|  For remote sessions, sent for each request that could not be made to restart the session.   
  
Show WSDL type definition

  
  
  



Sends a message to a session. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_MANAGE_VDI_SESSION|  Machine session management with the corresponding access group permission is sufficient to send a message to a session.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to to send a message to a session.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  unique identifier for session   
  
**msgType**|  xsd:string|  Message type: Warning, Info or Error   


  * This parameter will be one of:  
|  Value |  Description   
---|---  
"WARNING"| WARNING: Message is a warning  
"ERROR"| ERROR: Message is an error  
"INFO"| INFO: Message is an info  

  
**message**|  xsd:string|  Text in message   
  
  


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
ADMIN_SESSION_SENDMSG|  For local sessions, if the session was successfully sent the message.   
ADMIN_SESSION_SENDMSG_FAILED|  For local sessions, if the session could not be sent the message.   
VLSI_FEDERATED_DESKTOP_SESSION_SEND_MESSAGE_REQUEST_SENT|  For remote sessions, if a request was successfully made to send a message to the session.   
VLSI_FEDERATED_DESKTOP_SESSION_SEND_MESSAGE_REQUEST_SEND_FAILED|  For remote sessions, if a request could not be made to send a message to the session.   
  
Show WSDL type definition

  
  
  



Sends a message to multiple sessions. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_MANAGE_VDI_SESSION|  Machine session management with the corresponding access group permission is sufficient to send a message to a session.   
FEDERATED_SESSIONS_MANAGE|  Global session management is sufficient to to send a message to a session.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Session](vdi.users.Session.md) used to make the method call.   
**ids**| [SessionId[]](vdi.entity.SessionId.md)|  unique identifiers for the sessions   
  
**msgType**|  xsd:string|  Message type: Warning, Info or Error   


  * This parameter will be one of:  
|  Value |  Description   
---|---  
"WARNING"| WARNING: Message is a warning  
"ERROR"| ERROR: Message is an error  
"INFO"| INFO: Message is an info  

  
**message**|  xsd:string|  Text in message   
  
  


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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| The index of the fault will contain null on success for the corresponding index of the sessionId or an exception if an error occurred. This exception will be an EntityNotFound if the session is not found.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_SESSION_SENDMSG|  For local sessions, sent for each session that was successfully sent a message.   
ADMIN_SESSION_SENDMSG_FAILED|  For local sessions, sent for each session that could not be sent a message.   
VLSI_FEDERATED_DESKTOP_SESSION_SEND_MESSAGE_REQUEST_SENT|  For remote sessions, sent for each request that was successfully made to send a message to the session.   
VLSI_FEDERATED_DESKTOP_SESSION_SEND_MESSAGE_REQUEST_SEND_FAILED|  For remote sessions, sent for each request that could not be made to send a message to the session.   
  
Show WSDL type definition

  
  
  
  
  
  
  
