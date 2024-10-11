---
layout: page
title: Data Object - UnderConstructionCount
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.UnderConstructionCount`

Property of  
> [RDSServerStateCount](vdi.resources.RDSServer.RDSServerStateCount.md#field_detail)

Since  
> Horizon 8.4


## Data Object Description 

Number of the RDS server machines which are in under construction states. Such machine's [status](vdi.resources.RDSServer.RDSServerStateView.md#status) is one of the following : PROVISIONING,CUSTOMIZING,MAINTENANCE,DELETING,WAIT_FOR_AGENT,AGENT_ERR_STARTUP_IN_PROGRESS, AGENT_DRAIN_MODE,AGENT_DRAIN_UNTIL_RESTART,DISABLED,DISABLE_IN_PROGRESS,VALIDATING 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**provisioning**|  xsd:int|  Number of RDS server machines which are in PROVISIONING [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**customizing**|  xsd:int|  Number of RDS server machines which are in CUSTOMIZING [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**maintenance**|  xsd:int|  Number of RDS server machines which are in MAINTENANCE [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**deleting**|  xsd:int|  Number of RDS server machines which are in DELETING [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**drainModeEnabled**|  xsd:int|  Number of RDS server machines which are in AGENT_DRAIN_MODE [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**drainModeRestart**|  xsd:int|  Number of RDS server machines which are in AGENT_DRAIN_UNTIL_RESTART [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**disabled**|  xsd:int|  Number of RDS server machines which are in DISABLED [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**disableProgress**|  xsd:int|  Number of RDS server machines which are in DISABLE_IN_PROGRESS [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**waitForAgent**|  xsd:int|  Number of RDS server machines which are in WAIT_FOR_AGENT [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**startupProgress**|  xsd:int|  Number of RDS server machines which are in AGENT_ERR_STARTUP_IN_PROGRESS [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**validating**|  xsd:int|  Number of RDS server machines which are in VALIDATING [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
  
  
   
  
  
