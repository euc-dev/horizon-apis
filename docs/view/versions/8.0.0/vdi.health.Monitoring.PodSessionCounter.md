---
layout: page
title: Data Object - PodSessionCounter
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.Monitoring.PodSessionCounter`

Returned by
> [Monitoring_ListPodSessionCounters](vdi.health.Monitoring.md#listPodSessionCounters)

See also
> [PodId](vdi.entity.PodId.md)

Since
> Horizon 7.12


## Data Object Description

Information about global sessions related to a Pod.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**podId**| [PodId](vdi.entity.PodId.md)|  Pod id. [^2]
**podName**|  xsd:string|  Name of the pod. [^2]
**localPod**|  xsd:boolean|  Indicates if the counter details belong the local POD. This is going to be true for only one POD in the Federation. [^2]
**numBrokeredSessions**|  xsd:int|  Total number of brokered global sessions. [^1] [^2]
**numHostedSessions**|  xsd:int|  Total number of hosted global sessions. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.