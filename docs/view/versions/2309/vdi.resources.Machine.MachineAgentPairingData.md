---
layout: page
title: Data Object - MachineAgentPairingData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineAgentPairingData  
Property of
     [MachineDetailsView](vdi.resources.Machine.MachineDetailsView.md#field_detail), [MachineInfo](vdi.resources.Machine.MachineInfo.md#field_detail)  
Since 
    Horizon 7.5

## Data Object Description 

Agent pairing data for this Machine. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**pairingState**|  xsd:string|  Agent pairing state.   


 * This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"NOT_AVAILABLE"| Agent pairing state is not available.  
"IN_PAIRING"| Agent pairing with connection server is in progress.  
"PAIRED_AND_SECURED"| Agent is paired and secured with a Connection Server.  

  
**configuredByBroker**|  xsd:string|  Name of the connection server the agent is paired with.   


 * This property need not be set.

  
**attemptedTheftByBroker**|  xsd:string|  Name of the connection server that attempted theft of pairing for this Agent.   


 * This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

