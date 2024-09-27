---
layout: page
title: Data Object - VirtualCenterHealthHostData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.VirtualCenterHealth.HostData  
Property of
     [VirtualCenterHealthInfo](vdi.health.VirtualCenterHealth.VirtualCenterHealthInfo.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Health information on a specific host managed by the Virtual Center server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The name of the Virtual Center host.   
  
**version**|  xsd:string|  The version of the Virtual Center host.   


 * This property need not be set.

  
**apiVersion**|  xsd:string|  The version of the API of the Virtual Center host.   


 * This property need not be set.

  
**status**|  xsd:string|  The status of the Virtual Center host.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTED"| The host is successfully connected to Virtual Center server.  
"DISCONNECTED"| The host is disconnected from Virtual Center server.  
"NOT_RESPONDING"| The host is not responding.  

  
**clusterName**|  xsd:string|  The name of the cluster of this Virtual Center host.   


 * This property need not be set.

  
**vGPUTypes**|  xsd:string[]|  Types of NVIDIA GRID vGPUs supported by this host.  **_Since_** Horizon View 6.1  


 * This property need not be set.
  * This property is an unordered array of unique values.

  
**numCpuCores**|  xsd:int|  Number of physical CPU cores on the host.  **_Since_** Horizon 7.7  


 * This property need not be set.

  
**cpuMhz**|  xsd:int|  CPU speed per core. This might be an averaged value if the speed is not uniform across all cores. The total CPU speed of the box is defined as cpuMhz * numCpuCores  **_Since_** Horizon 7.7  


 * This property need not be set.

  
**overallCpuUsage**|  xsd:int| **Deprecated.**_This does not provide proper value of CPU usage and should not be used._ Aggregated CPU usage across all cores on the host in MHz.  **_Since_** Horizon 7.7  


 * This property need not be set.

  
**memorySizeBytes**|  xsd:long|  The physical memory size in bytes.  **_Since_** Horizon 7.7  


 * This property need not be set.

  
**overallMemoryUsageMB**|  xsd:int| **Deprecated.**_This does not provide proper value of Memory usage and should not be used._ Physical memory usage on the host in MB.  **_Since_** Horizon 7.7  


 * This property need not be set.

  
**numMachines**|  xsd:int|  Number of machines provisioned on the host.  **_Since_** Horizon 7.10  


 * This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

