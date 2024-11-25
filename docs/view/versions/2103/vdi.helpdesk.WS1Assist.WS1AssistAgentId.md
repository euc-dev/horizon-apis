---
layout: page
title: Data Object - WS1AssistAgentId
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.WS1Assist.WS1AssistAgentId`

Returned by
> [WS1Assist_GetWS1AssistAgentId](vdi.helpdesk.WS1Assist.md#getWS1AssistAgentId)

Since
> Horizon 8.2


## Data Object Description
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**agentId**|  xsd:string|  The agent ID for Workspace ONE Assist. [^1] [^2]
**errorCode**|  xsd:int|  Error code for failing to get agent ID. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>null</td><td>There is no error.</td></tr><tr><td>null</td><td>The View Agent version (Helpdesk Plugin) is lower than the required version.</td></tr><tr><td>null</td><td>The Workspace One Assist Agent isn't installed.</td></tr><tr><td>null</td><td>The Workspace One Assist Agent doesn't support this version of OS.</td></tr></table>




 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.