---
layout: page
title: Data Object - WS1AssistSessionSpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.WS1Assist.WS1AssistSessionSpec`

Parameter to
> [WS1Assist_GetWS1AssistAgentId](vdi.helpdesk.WS1Assist.md#getWS1AssistAgentId)

See also
> [SessionId](vdi.entity.SessionId.md)

Since
> Horizon 8.2


## Data Object Description
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**sessionId**| [SessionId](vdi.entity.SessionId.md)|  The session ID
**customerId**|  xsd:string|  The HCS customer Id.. [^2]
**tenantId**|  xsd:string|  The HCS tenant Id. [^2]
**ws1AssistServerUrl**|  xsd:string|  Workspace ONE Assist server url. [^2]
 


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.