---
layout: page
title: Data Object - LogCollectorComponentIdentifier
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.LogCollectorComponentIdentifier`

Property of
> [LogCollectorSpec](vdi.utils.logcollector.LogCollector.LogCollectorSpec.md#field_detail), [LogCollectorTaskInfo](vdi.utils.logcollector.LogCollector.LogCollectorTaskInfo.md#field_detail)

Parameter to
> [LogCollector_Purge](vdi.utils.logcollector.LogCollector.md#purge)

See also
> [ConnectionServerId](vdi.entity.ConnectionServerId.md), [MachineId](vdi.entity.MachineId.md), [RDSServerId](vdi.entity.RDSServerId.md)

Since
> Horizon 7.10


## Data Object Description

Represents identifier of a log collector component.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**logCollectorComponentType**|  xsd:string|  Type of the log collector component. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>CONNECTION_SERVER</td><td>Log component type is Connection Server.</td></tr><tr><td>AGENT</td><td>Log component type is agent machine from desktop pool.</td></tr><tr><td>AGENT_RDS</td><td>Log component type is agent RDSH server from farm.</td></tr></table>
**csId**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  Identifier of a connection server. [^1] [^154]
**machineId**| [MachineId](vdi.entity.MachineId.md)|  Identifier of a desktop pool machine.  **_Since_** Horizon 7.12 [^1] [^202]
**rdsServerId**| [RDSServerId](vdi.entity.RDSServerId.md)|  Identifier of a remote desktop services server.  **_Since_** Horizon 7.12 [^1] [^156]


 


[^1]: This property need not be set.
[^154]: This property is required if logCollectorComponentType is set to "CONNECTION_SERVER".
[^156]: This property is required if logCollectorComponentType is set to "AGENT_RDS".
[^202]: This property is required if logCollectorComponentType is set to "AGENT".