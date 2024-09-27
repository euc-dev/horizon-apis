---
layout: page
title: Service - WS1Assist
hide:
 #- navigation
 - toc
---

  
   
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.helpdesk.WS1Assist  
See also
     [SessionId](vdi.entity.SessionId.md), [WS1AssistAgentId](vdi.helpdesk.WS1Assist.WS1AssistAgentId.md), [WS1AssistAgentStatus](vdi.helpdesk.WS1Assist.WS1AssistAgentStatus.md), [WS1AssistSessionSpec](vdi.helpdesk.WS1Assist.WS1AssistSessionSpec.md)  
Since 
    Horizon 8.2

  


## Service Description

The service for fetching Workspace ONE Assist status or agent ID for a session. 

Methods

Methods defined in this Service   
---  
WS1Assist_GetWS1AgentAssistStatus, WS1Assist_GetWS1AssistAgentId  
  



Get the Workspace ONE Assist status from a session. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  Machine read with the corresponding access group permission is sufficient to get a session's Workspace ONE Assist status.   
POOL_VIEW|  Desktop read with the corresponding access group permission is sufficient to get a session's Workspace ONE Assist status.   
FEDERATED_SESSIONS_VIEW|  Global session read is sufficient to get a session's Workspace ONE Assist status.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [WS1Assist](vdi.helpdesk.WS1Assist.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionID .   
  
  


Return Value 

Type |  Description   
---|---  
[WS1AssistAgentStatus](vdi.helpdesk.WS1Assist.WS1AssistAgentStatus.md)| WS1AssistAgentStatus for the session.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Get the Workspace ONE Assist agent ID from a session. 

Privileges 

Privilege |  Description   
---|---  
REMOTE_ASSISTANCE|  privilege is required to get a Workspace ONE Assist token.   
MACHINE_MANAGEMENT|  is sufficient to get Workspace ONE Assist token.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [WS1Assist](vdi.helpdesk.WS1Assist.md) used to make the method call.   
**ws1AssistSessionSpec**| [WS1AssistSessionSpec](vdi.helpdesk.WS1Assist.WS1AssistSessionSpec.md)|    
  
  


Return Value 

Type |  Description   
---|---  
[WS1AssistAgentId](vdi.helpdesk.WS1Assist.WS1AssistAgentId.md)| WS1AssistAgentId for the session  
  


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
HELPDESK_GET_WS1_ASSIST_AGENT_ID|  For local sessions, if a Workspace ONE Assist agent ID is successfully obtained.   
  
Show WSDL type definition

  
  
  
  
  
  
  

