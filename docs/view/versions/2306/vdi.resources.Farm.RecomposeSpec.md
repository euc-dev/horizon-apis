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
  
**startTime**|  xsd:dateTime|  When to start the operation. If unset the operation will begin immediately.   


* This property need not be set.

  
**logoffSetting**|  xsd:string|  Determines when to perform the operation on RDS servers which have an active session.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"FORCE_LOGOFF"| Users will be forced to log off when the system is ready to operate on their RDS Servers. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).  
"WAIT_FOR_LOGOFF"| Wait for connected users to disconnect before the task starts. The operation starts immediately on RDS Servers without active sessions.  

  
**stopOnFirstError**|  xsd:boolean|  Indicates that the operation should stop on first error.   


  * This property has a default value of true.

  
**rdsServers**| [RDSServerId[]](vdi.entity.RDSServerId.md)|  The RDS Servers to recompose.   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
