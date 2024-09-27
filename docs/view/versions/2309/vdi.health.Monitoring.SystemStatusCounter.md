---
layout: page
title: Data Object - SystemStatusCounter
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.Monitoring.SystemStatusCounter  
Returned by
     [Monitoring_GetSystemStatusCounter](vdi.health.Monitoring.md#getSystemStatusCounter)  
See also
     [EventSeverityCounter](vdi.health.Monitoring.EventSeverityCounter.md), [HealthCounter](vdi.health.Monitoring.HealthCounter.md)  
Since 
    Horizon 7.12

## Data Object Description 

System status information. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**sessionsCount**|  xsd:int|  Number of active sessions.   


 * This property need not be set.
 * This property cannot be updated.

  
**problemVcenterVmsCount**|  xsd:int|  Number of the managed VMs which are in any of the following machine's [basicState](vdi.resources.Machine.MachineBase.md#basicState) states : AGENT_ERR_DISABLED, AGENT_UNREACHABLE, AGENT_ERR_INVALID_IP, AGENT_ERR_NEED_REBOOT, AGENT_ERR_PROTOCOL_FAILURE, AGENT_ERR_DOMAIN_FAILURE, AGENT_CONFIG_ERROR, PROVISIONING_ERROR, ERROR, UNASSIGNED_USER_CONNECTED, UNASSIGNED_USER_DISCONNECTED, UNKNOWN.   


 * This property need not be set.
 * This property cannot be updated.

  
**problemRDSHostsCount**|  xsd:int|  Number of RDS Hosts that are part of a farm and which are in any of the following [status](vdi.resources.RDSServer.RDSServerRuntimeData.md#status) states : AGENT_UNREACHABLE, AGENT_CONFIG_ERROR, UNKNOWN, ALREADY_USED, PROVISIONING_ERROR, ERROR and AGENT_ERR_PROTOCOL_FAILURE.   


 * This property need not be set.
 * This property cannot be updated.

  
**eventSeverityCounter**| [EventSeverityCounter](vdi.health.Monitoring.EventSeverityCounter.md)|  Event severity counter. This will be unset if Event database is not configured in the Pod.   


 * This property need not be set.
 * This property cannot be updated.

  
**healthCounter**| [HealthCounter](vdi.health.Monitoring.HealthCounter.md)|  The health status information.   


 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

