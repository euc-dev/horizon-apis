---
layout: page
title: Data Object - FarmRecomposeSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.RecomposeSpec`

Parameter to
> [Farm_Recompose](vdi.resources.Farm.md#recompose)

See also
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [RDSServerId](vdi.entity.RDSServerId.md)

Since
> Horizon View 6.2


## Data Object Description

Specification for the recompose operation.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**parentVm**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  New base image VM for automated farm's RDS Servers. This must be in the same datacenter as the base image of the RDS Server.
**snapshot**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  Base image snapshot for the Automated Farm's RDS Servers.
**startTime**|  xsd:dateTime|  When to start the operation. If unset the operation will begin immediately. [^1]
**logoffSetting**|  xsd:string|  Determines when to perform the operation on RDS servers which have an active session. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"FORCE_LOGOFF"</td><td>Users will be forced to log off when the system is ready to operate on their RDS Servers. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).</td></tr><tr><td>"WAIT_FOR_LOGOFF"</td><td>Wait for connected users to disconnect before the task starts. The operation starts immediately on RDS Servers without active sessions.</td></tr></table>
**stopOnFirstError**|  xsd:boolean|  Indicates that the operation should stop on first error. [^6]
**rdsServers**| [RDSServerId[]](vdi.entity.RDSServerId.md)|  The RDS Servers to recompose.
 


 


[^1]: This property need not be set.
[^6]: This property has a default value of true.