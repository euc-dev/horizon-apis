---
layout: page
title: Data Object - SystemStatusCounter
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.Monitoring.SystemStatusCounter`

Returned by
> [Monitoring_GetSystemStatusCounter](vdi.health.Monitoring.md#getSystemStatusCounter)

See also
> [EventSeverityCounter](vdi.health.Monitoring.EventSeverityCounter.md), [HealthCounter](vdi.health.Monitoring.HealthCounter.md)

Since
> Horizon 7.12


## Data Object Description

System status information.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**sessionsCount**|  xsd:int|  Number of active sessions. [^1] [^2]
**problemVcenterVmsCount**|  xsd:int|  Number of the managed VMs which are in any of the following machine's [basicState](vdi.resources.Machine.MachineBase.md#basicState) states : AGENT_ERR_DISABLED, AGENT_UNREACHABLE, AGENT_ERR_INVALID_IP, AGENT_ERR_NEED_REBOOT, AGENT_ERR_PROTOCOL_FAILURE, AGENT_ERR_DOMAIN_FAILURE, AGENT_CONFIG_ERROR, PROVISIONING_ERROR, ERROR, UNASSIGNED_USER_CONNECTED, UNASSIGNED_USER_DISCONNECTED, UNKNOWN. [^1] [^2]
**problemRDSHostsCount**|  xsd:int|  Number of RDS Hosts that are part of a farm and which are in any of the following [status](vdi.resources.RDSServer.RDSServerRuntimeData.md#status) states : AGENT_UNREACHABLE, AGENT_CONFIG_ERROR, UNKNOWN, ALREADY_USED, PROVISIONING_ERROR, ERROR and AGENT_ERR_PROTOCOL_FAILURE. [^1] [^2]
**eventSeverityCounter**| [EventSeverityCounter](vdi.health.Monitoring.EventSeverityCounter.md)|  Event severity counter. This will be unset if Event database is not configured in the Pod. [^1] [^2]
**healthCounter**| [HealthCounter](vdi.health.Monitoring.HealthCounter.md)|  The health status information. [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.