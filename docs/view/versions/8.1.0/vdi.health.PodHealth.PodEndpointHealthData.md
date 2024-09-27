---
layout: page
title: Data Object - PodEndpointHealthData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.PodHealth.PodEndpointHealthData  
Property of
     [PodHealthData](vdi.health.PodHealth.PodHealthData.md#field_detail)  
See also
     [PodEndpointInfo](vdi.federation.PodEndpoint.PodEndpointInfo.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Pod endpoint health data. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**endpointInfo**| [PodEndpointInfo](vdi.federation.PodEndpoint.PodEndpointInfo.md)|  The PodEndpointInfo   


* This property cannot be updated.

  
**state**|  xsd:string|  Health state of this PodEndpoint   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"ONLINE"| PodEndpoint is online and functional.  
"UNCHECKED"| PodEndpoint was offline and it just came back online but the system has not verified that it is functional.  
"OFFLINE"| PodEndpoint is offline or unreachable.  

  
**roundTripTime**|  xsd:long|  Round trip time (in milliseconds) for ping request between the local podEndpoint and the remote pod.   


* This property need not be set.
* This property cannot be updated.

  
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12  


* This property need not be set.
* This property cannot be updated.

  
  
  
  
  
  

