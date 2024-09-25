---
layout: page
title: Data Object - MachineSessionData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineSessionData
Property of
     [MachineDetailsView](vdi.resources.Machine.MachineDetailsView.md#field_detail)
See also
     [SessionId](vdi.entity.SessionId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)
Since 
    Horizon 7.7

## Data Object Description 

Session data on the Machine. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [SessionId](vdi.entity.SessionId.md)|  Session id.   


[^2]

  
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Id of the user involved in this session.   


[^2]

  
**userName**|  xsd:string|  Name of the user involved in this session.   


[^2]

  
**sessionProtocol**|  xsd:string|  Protocol for this session. This will be unset for disconnected sessions.   


[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"PCOIP"| Display protocol is PCoIP  
"RDP"| Display protocol is RDP  
"BLAST"| Display protocol is Blast  
"CONSOLE"| Display protocol is Console  
"UNKNOWN"| Display protocol is unknown  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

