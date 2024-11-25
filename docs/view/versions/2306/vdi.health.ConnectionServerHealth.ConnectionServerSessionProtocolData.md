---
layout: page
title: Data Object - ConnectionServerSessionProtocolData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.ConnectionServerHealth.ConnectionServerSessionProtocolData`

Property of
> [ConnectionServerHealthInfo](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md#field_detail)

Since
> Horizon 7.10


## Data Object Description

Information about the protocol sessions of the connection server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**sessionProtocol**|  xsd:string|  Protocol used to launch the session.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"PCOIP"</td><td>Display protocol is PCoIP.</td></tr><tr><td>"RDP"</td><td>Display protocol is RDP.</td></tr><tr><td>"BLAST"</td><td>Display protocol is Blast.</td></tr></table>
**numSessions**|  xsd:int|  Number of active sessions launched using [sessionProtocol](vdi.health.ConnectionServerHealth.ConnectionServerSessionProtocolData.md#sessionProtocol).
 


 
