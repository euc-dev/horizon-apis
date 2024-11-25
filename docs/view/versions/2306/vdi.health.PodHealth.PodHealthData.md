---
layout: page
title: Data Object - PodHealthData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.PodHealth.PodHealthData`

Property of
> [PodHealthInfo](vdi.health.PodHealth.PodHealthInfo.md#field_detail)

See also
> [PodEndpointHealthData](vdi.health.PodHealth.PodEndpointHealthData.md), [SiteId](vdi.entity.SiteId.md)

Since
> Horizon View 6.0


## Data Object Description

Pod Health data.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**site**| [SiteId](vdi.entity.SiteId.md)|  The Id of the site this pod belongs to [^2]
**endpointHealth**| [PodEndpointHealthData[]](vdi.health.PodHealth.PodEndpointHealthData.md)|  Health data for the the podEndpoints in this pod [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.