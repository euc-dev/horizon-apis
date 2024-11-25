---
layout: page
title: Data Object - MachineSessionData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.MachineSessionData`

Property of
> [MachineDetailsView](vdi.resources.Machine.MachineDetailsView.md#field_detail)

See also
> [SessionId](vdi.entity.SessionId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon 7.7


## Data Object Description

Session data on the Machine.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [SessionId](vdi.entity.SessionId.md)|  Session id. [^2]
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Id of the user involved in this session. [^2]
**userName**|  xsd:string|  Name of the user involved in this session. [^2]
**sessionProtocol**|  xsd:string|  Protocol for this session. This will be unset for disconnected sessions. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"PCOIP"</td><td>Display protocol is PCoIP</td></tr><tr><td>"RDP"</td><td>Display protocol is RDP</td></tr><tr><td>"BLAST"</td><td>Display protocol is Blast</td></tr><tr><td>"CONSOLE"</td><td>Display protocol is Console</td></tr><tr><td>"ULTRA"</td><td>Display protocol is PCoIP Ultra</td></tr><tr><td>"UNKNOWN"</td><td>Display protocol is unknown</td></tr></table>




 


[^1]: This property need not be set.
[^2]: This property cannot be updated.