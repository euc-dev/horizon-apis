---
layout: page
title: Data Object - WS1AssistAgentId
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.helpdesk.WS1Assist.WS1AssistAgentId
Returned by
     [WS1Assist_GetWS1AssistAgentId](vdi.helpdesk.WS1Assist.md#getWS1AssistAgentId)
Since 
    Horizon 8.2

## Data Object Description 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**agentId**|  xsd:string|  The agent ID for Workspace ONE Assist.   


[^1]
[^2]

  
**errorCode**|  xsd:int|  Error code for failing to get agent ID.   


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
null| There is no error.  
null| the View Agent version (Helpdesk Plugin) is lower than required version.  
null| The Workspace One Assist Agent isn't installed.  
null| The Workspace One Assist Agent doesn't support this version of OS.  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

