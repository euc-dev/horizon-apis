---
layout: page
title: Data Object - MachineSessionData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineSessionData`

Property of  
> [MachineDetailsView](vdi.resources.Machine.MachineDetailsView.md#field_detail)

See also  
> [SessionId](vdi.entity.SessionId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since  
> Horizon 7.7


## Data Object Description 

Session data on the Machine. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [SessionId](vdi.entity.SessionId.md)|  Session id.   


* This property cannot be updated.

  
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Id of the user involved in this session.   


* This property cannot be updated.

  
**userName**|  xsd:string|  Name of the user involved in this session.   


* This property cannot be updated.

  
**sessionProtocol**|  xsd:string|  Protocol for this session. This will be unset for disconnected sessions.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"PCOIP"| Display protocol is PCoIP  
"RDP"| Display protocol is RDP  
"BLAST"| Display protocol is Blast  
"CONSOLE"| Display protocol is Console  
"UNKNOWN"| Display protocol is unknown  

  
  
  

  
  
