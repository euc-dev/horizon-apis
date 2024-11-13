---
layout: page
title: Data Object - PodEndpointHealthData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.health.PodHealth.PodEndpointHealthData`

Property of
> [PodHealthData](vdi.health.PodHealth.PodHealthData.md#field_detail)

See also
> [PodEndpointInfo](vdi.federation.PodEndpoint.PodEndpointInfo.md)

Since
> Horizon View 6.0


## Data Object Description

Pod endpoint health data.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**endpointInfo**| [PodEndpointInfo](vdi.federation.PodEndpoint.PodEndpointInfo.md)|  The PodEndpointInfo [^2]
**state**|  xsd:string|  Health state of this PodEndpoint [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"ONLINE"</td><td>PodEndpoint is online and functional.</td></tr><tr><td>"UNCHECKED"</td><td>PodEndpoint was offline and it just came back online but the system has not verified that it is functional.</td></tr><tr><td>"OFFLINE"</td><td>PodEndpoint is offline or unreachable.</td></tr></table>
**roundTripTime**|  xsd:long|  Round trip time (in milliseconds) for ping request between the local podEndpoint and the remote pod. [^1] [^2]
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.