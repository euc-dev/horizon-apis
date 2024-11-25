---
layout: page
title: Data Object - VirtualCenterHealthHostData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.VirtualCenterHealth.HostData`

Property of
> [VirtualCenterHealthInfo](vdi.health.VirtualCenterHealth.VirtualCenterHealthInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Health information on a specific host managed by the Virtual Center server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  The name of the Virtual Center host.
**version**|  xsd:string|  The version of the Virtual Center host. [^1]
**apiVersion**|  xsd:string|  The version of the API of the Virtual Center host. [^1]
**status**|  xsd:string|  The status of the Virtual Center host.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"CONNECTED"</td><td>The host is successfully connected to Virtual Center server.</td></tr><tr><td>"DISCONNECTED"</td><td>The host is disconnected from Virtual Center server.</td></tr><tr><td>"NOT_RESPONDING"</td><td>The host is not responding.</td></tr></table>
**clusterName**|  xsd:string|  The name of the cluster of this Virtual Center host. [^1]
**vGPUTypes**|  xsd:string[]|  Types of NVIDIA GRID vGPUs supported by this host.  **_Since_** Horizon View 6.1 [^1] [^14]
**numCpuCores**|  xsd:int|  Number of physical CPU cores on the host.  **_Since_** Horizon 7.7 [^1]
**cpuMhz**|  xsd:int|  CPU speed per core. This might be an averaged value if the speed is not uniform across all cores. The total CPU speed of the box is defined as cpuMhz * numCpuCores  **_Since_** Horizon 7.7 [^1]
**overallCpuUsage**|  xsd:int| **Deprecated.**_This does not provide proper value of CPU usage and should not be used._ Aggregated CPU usage across all cores on the host in MHz.  **_Since_** Horizon 7.7 [^1]
**memorySizeBytes**|  xsd:long|  The physical memory size in bytes.  **_Since_** Horizon 7.7 [^1]
**overallMemoryUsageMB**|  xsd:int| **Deprecated.**_This does not provide proper value of Memory usage and should not be used._ Physical memory usage on the host in MB.  **_Since_** Horizon 7.7 [^1]
**numMachines**|  xsd:int|  Number of machines provisioned on the host.  **_Since_** Horizon 7.10 [^1]


 


[^1]: This property need not be set.
[^14]: This property is an unordered array of unique values.