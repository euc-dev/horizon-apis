---
layout: page
title: Data Object - ConnectionServerSessionProtocolData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.ConnectionServerHealth.ConnectionServerSessionProtocolData  
Property of
     [ConnectionServerHealthInfo](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md#field_detail)  
Since 
    Horizon 7.10

## Data Object Description 

Information about the protocol sessions of the connection server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**sessionProtocol**|  xsd:string|  Protocol used to launch the session.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"PCOIP"| Display protocol is PCoIP  
"RDP"| Display protocol is RDP  
"BLAST"| Display protocol is Blast  

  
**numSessions**|  xsd:int|  Number of active sessions launched using [sessionProtocol](vdi.health.ConnectionServerHealth.ConnectionServerSessionProtocolData.md#sessionProtocol).   
  
  
  

  
  

