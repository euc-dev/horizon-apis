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


* This property need not be set.

  
**hostData**| [VirtualCenterHealthHostData[]](vdi.health.VirtualCenterHealth.HostData.md)|  Health information about each host managed by the Virtual Center server.   


* This property need not be set.

  
**datastoreData**| [VirtualCenterHealthDatastoreData[]](vdi.health.VirtualCenterHealth.DatastoreData.md)|  Health information about each datastore managed by the Virtual Center server.   


* This property need not be set.

  
**refId**|  xsd:string|  Reference ID of the Virtual Center server.  **_Since_** Horizon 7.10  


* This property need not be set.

  
  
  
   
  
  

