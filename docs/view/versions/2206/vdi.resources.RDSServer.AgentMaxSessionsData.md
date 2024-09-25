---
layout: page
title: Data Object - RDSServerAgentMaxSessionsData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.AgentMaxSessionsData
Property of
     [RDSServerSettings](vdi.resources.RDSServer.RDSServerSettings.md#field_detail)
Since 
    Horizon View 6.0

## Data Object Description 

Agent max number of sessions 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**maxSessionsType**|  xsd:string|  RDSServer max sessions type as reported by the agent   


  * This property has a default value of "LIMITED".
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"UNLIMITED"| RDSServer has unlimited number of sessions  
"LIMITED"| RDSServer has a limited number of sessions  

  
**maxSessionsSeenByAgent**|  xsd:int|  Maximum number of sessions on an RDS server as seen by the agent.   


[^1]
[^2]
  * This property has a minimum value of 1. 
  * This property is required if maxSessionsType is set to "LIMITED".

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
