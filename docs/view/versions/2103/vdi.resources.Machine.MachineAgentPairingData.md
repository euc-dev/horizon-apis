---
layout: page
title: Data Object - MachineAgentPairingData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.MachineAgentPairingData`

Property of
> [MachineDetailsView](vdi.resources.Machine.MachineDetailsView.md#field_detail), [MachineInfo](vdi.resources.Machine.MachineInfo.md#field_detail)

Since
> Horizon 7.5


## Data Object Description

Agent pairing data for this Machine.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**pairingState**|  xsd:string|  Agent pairing state. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"NOT_AVAILABLE"</td><td>Agent pairing state is not available.</td></tr><tr><td>"IN_PAIRING"</td><td>Agent pairing with connection server is in progress.</td></tr><tr><td>"PAIRED_AND_SECURED"</td><td>Agent is paired and secured with a Connection Server.</td></tr></table>
**configuredByBroker**|  xsd:string|  Name of the connection server the agent is paired with. [^1]
**attemptedTheftByBroker**|  xsd:string|  Name of the connection server that attempted theft of pairing for this Agent. [^1]


 


[^1]: This property need not be set.