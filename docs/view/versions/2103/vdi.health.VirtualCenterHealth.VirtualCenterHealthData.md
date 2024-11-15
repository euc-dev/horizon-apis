---
layout: page
title: Data Object - VirtualCenterHealthData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.VirtualCenterHealth.VirtualCenterHealthData`

Property of
> [VirtualCenterHealthInfo](vdi.health.VirtualCenterHealth.VirtualCenterHealthInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Basic data about the virtual center server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  The name of the Virtual Center server. [^1]
**version**|  xsd:string|  The version of the Virtual Center server. [^1]
**build**|  xsd:string|  The build of the Virtual Center server. [^1]
**apiVersion**|  xsd:string|  The version of the API used to communicate with the Virtual Center server. [^1]
**instanceUuid**|  xsd:string|  Virtual center instanceUuid.  **_Since_** Horizon 7.8 [^1]
**viewComposerConfigured**|  xsd:boolean| **Deprecated.**_This property is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ Whether view composer is added or not.  **_Since_** Horizon 7.10 [^5]
**numDesktops**|  xsd:int|  Number of Desktops managed by the virtual center.  **_Since_** Horizon 7.10 [^1]
**numMachines**|  xsd:int|  Number of Machines managed by the virtual center.  **_Since_** Horizon 7.10 [^1]


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.