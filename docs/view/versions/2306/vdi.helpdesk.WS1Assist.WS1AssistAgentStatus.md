---
layout: page
title: Data Object - WS1AssistAgentStatus
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.WS1Assist.WS1AssistAgentStatus`

Returned by
> [WS1Assist_GetWS1AgentAssistStatus](vdi.helpdesk.WS1Assist.md#getWS1AssistAgentStatus)

Since
> Horizon 8.2


## Data Object Description
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**statusCode**|  xsd:int|  The status code of Workspace ONE Assist. [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>null</td><td>There is no error.</td></tr><tr><td>null</td><td>The View Agent version (Helpdesk Plugin) is lower than required version.</td></tr><tr><td>null</td><td>The Workspace One Assist Agent isn't installed.</td></tr><tr><td>null</td><td>The Workspace One Assist Agent doesn't support this version of OS.</td></tr></table>
 


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.