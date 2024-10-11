---
layout: page
title: Data Object - RDSHLoadBalancingSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.LoadBalancingSettings`

Property of  
> [FarmData](vdi.resources.Farm.FarmData.md#field_detail)

See also  
> [RDSHLoadBalancingMetricsSettings](vdi.resources.Farm.LoadBalancingMetricsSettings.md)

Since  
> Horizon 7.8


## Data Object Description 

RDSH Load Balancing Settings 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**useCustomScript**|  xsd:boolean|  Represents whether to use custom scripts for Load Balancing.   


  * This property has a default value of false.
 * This property need not be set.

  
**connectingSessionThreshold**|  xsd:int|  This value will be used for handling logon storm. The configured threshold specifies the maximum number of sessions that can concurrently log into each RDSH agent machine in the farm, exempting reconnecting sessions. By default, this threshold is disabled and does not deny session logins.  **_Since_** Horizon 8.4  


  * This property has a default value of 0.
 * This property need not be set.
  * This property has a minimum value of 0. 
  * This property has a maximum value of 150. 

  
**loadIndexThreshold**|  xsd:int|  This value will be used for handling logon storm. The configured threshold specifies the minimum load index at which each RDSH agent machine in the farm will start denying session logins, exempting reconnecting sessions. By default, this threshold is disabled and does not deny session logins.  **_Since_** Horizon 8.4  


  * This property has a default value of 0.
 * This property need not be set.
  * This property has a minimum value of 0. 
  * This property has a maximum value of 100. 

  
**lbMetricsSettings**| [RDSHLoadBalancingMetricsSettings](vdi.resources.Farm.LoadBalancingMetricsSettings.md)|  Metrics used for load balancing. This will be used only when [useCustomScript](vdi.resources.Farm.LoadBalancingSettings.md#useCustomScript) is set to false.   


 * This property need not be set.
  * This property is required if useCustomScript is set to false.

  
  

  
