---
layout: page
title: Data Object - PodHealthInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.PodHealth.PodHealthInfo`

Returned by
> [PodHealth_Get](vdi.health.PodHealth.md#get), [PodHealth_List](vdi.health.PodHealth.md#list)

See also
> [PodHealthData](vdi.health.PodHealth.PodHealthData.md), [PodId](vdi.entity.PodId.md)

Since
> Horizon View 6.0


## Data Object Description

Info object for PodHealth

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [PodId](vdi.entity.PodId.md)|  Id for the Pod [^2]
**displayName**|  xsd:string|  Display name for the pod.  **_Since_** Horizon 7.9 [^1] [^2]
**data**| [PodHealthData](vdi.health.PodHealth.PodHealthData.md)|  Health data for this pod. [^2]
**refId**|  xsd:string|  Reference ID used for this pod.  **_Since_** Horizon 7.11 [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.