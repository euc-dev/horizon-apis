---
layout: page
title: Data Object - FarmData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.FarmData
Property of
     [FarmInfo](vdi.resources.Farm.FarmInfo.md#field_detail), [FarmSpec](vdi.resources.Farm.FarmSpec.md#field_detail)
See also
     [AccessGroupId](vdi.entity.AccessGroupId.md), [DesktopId](vdi.entity.DesktopId.md), [FarmDisplayProtocolSettings](vdi.resources.Farm.DisplayProtocolSettings.md), [FarmMirageConfigurationOverrides](vdi.resources.Farm.MirageConfigurationOverrides.md), [FarmSessionSettings](vdi.resources.Farm.SessionSettings.md), [RDSHLoadBalancingSettings](vdi.resources.Farm.LoadBalancingSettings.md)
Since 
    Horizon View 6.0

## Data Object Description 

Farm data 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Farm name   


[^2]
  * This property must contain only alphanumerics, underscores, and dashes. The maximum length is 64 characters. 

  
**displayName**|  xsd:string|  Farm display name. If the display name is left blank, it defaults to [name](vdi.resources.Farm.FarmData.md#name)   


[^1]
  * This property has a maximum length of 256 characters. 

  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  View access groups can organize the farms in your organization. They can also be used for delegated administration.   
  
**description**|  xsd:string|  Farm description   


[^1]
  * This property has a maximum length of 1024 characters. 

  
**enabled**|  xsd:boolean|  Indicates if Farm is enabled   


  * This property has a default value of true.
[^1]

  
**deleting**|  xsd:boolean|  True if the farm is in the process of being deleted. This cannot be set or updated. Only applicable for automated farms.  **_Since_** Horizon View 6.2  


  * This property has a default value of false.
[^2]

  
**settings**| [FarmSessionSettings](vdi.resources.Farm.SessionSettings.md)|  Farm settings   


[^1]

  
**lbSettings**| [RDSHLoadBalancingSettings](vdi.resources.Farm.LoadBalancingSettings.md)|  Settings for load balancing the session requests across the RDS hosts in the farm  **_Since_** Horizon 7.8  


[^1]

  
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  Entity ID of RDS Desktop in the Farm   


[^1]
[^2]

  
**displayProtocolSettings**| [FarmDisplayProtocolSettings](vdi.resources.Farm.DisplayProtocolSettings.md)|  Farm Display Protocol settings   


[^1]

  
**serverErrorThreshold**|  xsd:int|  The minimum number of machines that must be fully operational in order to avoid showing the farm in an error state   


  * This property has a default value of 0.
[^1]
  * This property has a minimum value of 0. 

  
**mirageConfigurationOverrides**| [FarmMirageConfigurationOverrides](vdi.resources.Farm.MirageConfigurationOverrides.md)|  The Mirage configuration overrides for this Farm.   


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

