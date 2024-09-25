---
layout: page
title: Data Object - VirtualCenterHealthInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.VirtualCenterHealth.VirtualCenterHealthInfo
Returned by
     [VirtualCenterHealth_Get](vdi.health.VirtualCenterHealth.md#get), [VirtualCenterHealth_List](vdi.health.VirtualCenterHealth.md#list)
See also
     [VirtualCenterHealthConnectionServerConnectionData](vdi.health.VirtualCenterHealth.ConnectionServerConnectionData.md), [VirtualCenterHealthData](vdi.health.VirtualCenterHealth.VirtualCenterHealthData.md), [VirtualCenterHealthDatastoreData](vdi.health.VirtualCenterHealth.DatastoreData.md), [VirtualCenterHealthHostData](vdi.health.VirtualCenterHealth.HostData.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Health information for a Virtual Center server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  The ID of the virtual center server.   
  
**data**| [VirtualCenterHealthData](vdi.health.VirtualCenterHealth.VirtualCenterHealthData.md)|  Basic information about the Virtual Center server.   
  
**connectionServerData**| [VirtualCenterHealthConnectionServerConnectionData[]](vdi.health.VirtualCenterHealth.ConnectionServerConnectionData.md)|  Information about the VC connections from each connection server.   


[^1]

  
**hostData**| [VirtualCenterHealthHostData[]](vdi.health.VirtualCenterHealth.HostData.md)|  Health information about each host managed by the Virtual Center server.   


[^1]

  
**datastoreData**| [VirtualCenterHealthDatastoreData[]](vdi.health.VirtualCenterHealth.DatastoreData.md)|  Health information about each datastore managed by the Virtual Center server.   


[^1]

  
**refId**|  xsd:string|  Reference ID of the Virtual Center server.  **_Since_** Horizon 7.10  


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
