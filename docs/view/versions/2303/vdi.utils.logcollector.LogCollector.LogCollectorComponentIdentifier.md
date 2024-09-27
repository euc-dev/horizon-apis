---
layout: page
title: Data Object - LogCollectorComponentIdentifier
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.LogCollectorComponentIdentifier  
Property of
     [LogCollectorSpec](vdi.utils.logcollector.LogCollector.LogCollectorSpec.md#field_detail), [LogCollectorTaskInfo](vdi.utils.logcollector.LogCollector.LogCollectorTaskInfo.md#field_detail), [LogLevelInfo](vdi.utils.logcollector.LogCollector.LogLevelInfo.md#field_detail), [LogLevelSpec](vdi.utils.logcollector.LogCollector.LogLevelSpec.md#field_detail)  
Parameter to
     [LogCollector_GetLogLevels](vdi.utils.logcollector.LogCollector.md#getLogLevels), [LogCollector_Purge](vdi.utils.logcollector.LogCollector.md#purge)  
See also
     [ConnectionServerId](vdi.entity.ConnectionServerId.md), [MachineId](vdi.entity.MachineId.md), [RDSServerId](vdi.entity.RDSServerId.md)  
Since 
    Horizon 7.10

## Data Object Description 

Represents identifier of a log collector component. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**logCollectorComponentType**|  xsd:string|  Type of the log collector component.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTION_SERVER"| Log component type is Connection Server.  
"AGENT"| Log component type is agent machine from desktop pool.  
"AGENT_RDS"| Log component type is agent RDSH server from farm.  

  
**csId**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  Identifier of a connection server.   


* This property need not be set.
  * This property is required if logCollectorComponentType is set to "CONNECTION_SERVER".

  
**machineId**| [MachineId](vdi.entity.MachineId.md)|  Identifier of a desktop pool machine.  **_Since_** Horizon 7.12  


* This property need not be set.
  * This property is required if logCollectorComponentType is set to "AGENT".

  
**rdsServerId**| [RDSServerId](vdi.entity.RDSServerId.md)|  Identifier of a remote desktop services server.  **_Since_** Horizon 7.12  


* This property need not be set.
  * This property is required if logCollectorComponentType is set to "AGENT_RDS".

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

