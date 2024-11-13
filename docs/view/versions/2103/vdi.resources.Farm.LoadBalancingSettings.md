---
layout: page
title: Data Object - RDSHLoadBalancingSettings
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.LoadBalancingSettings`

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
**useCustomScript**|  xsd:boolean|  Represents whether to use custom scripts for Load Balancing. [^5] [^1]
**lbMetricsSettings**| [RDSHLoadBalancingMetricsSettings](vdi.resources.Farm.LoadBalancingMetricsSettings.md)|  Metrics used for load balancing. This will be used only when [useCustomScript](vdi.resources.Farm.LoadBalancingSettings.md#useCustomScript) is set to false. [^1] [^117]


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^117]: This property is required if useCustomScript is set to false.