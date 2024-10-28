---
layout: page
title: Data Object - PodEndpointInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.federation.PodEndpoint.PodEndpointInfo`

Property of
> [PodEndpointHealthData](vdi.health.PodHealth.PodEndpointHealthData.md#field_detail)

Returned by
> [PodEndpoint_Get](vdi.federation.PodEndpoint.md#get), [PodEndpoint_List](vdi.federation.PodEndpoint.md#list)

See also
> [PodEndpointId](vdi.entity.PodEndpointId.md)

Since
> Horizon View 6.0


## Data Object Description

Info object for the PodEndpoint.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [PodEndpointId](vdi.entity.PodEndpointId.md)|  Unique identifier for a PodEndpoint [^2]
**name**|  xsd:string|  Name for the podEndpoint [^2]
**serverAddress**|  xsd:string|  The URL for the PodEndpoint. This address and special port will be used for inter-pod communication. [^2]
**enabled**|  xsd:boolean|  Indicate whether an endpoint is enabled. A disabled endpoint will be excluded from participating inter-pod communication. [^2]
**refId**|  xsd:string|  Reference ID used for this PodEndpoint.  **_Since_** Horizon 7.11 [^1]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.