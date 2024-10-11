---
layout: page
title: Data Object - GlobalFeatureSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.FeatureSettings`

Property of  
> [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md#field_detail)

Returned by  
> [GlobalSettings_GetFeatureSettings](vdi.infrastructure.GlobalSettings.md#getFeatureSettings)

Since  
> Horizon 7.5


## Data Object Description 

Feature settings. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**enableHelpdesk**|  xsd:boolean|  Determines whether help desk feature is enabled or not. By default enableHelpdesk is true and helpdesk would be enabled.   


  * This property has a default value of true.
* This property need not be set.
* This property cannot be updated.

  
**enableImageManagement**|  xsd:boolean|  Determines whether Image Management feature is enabled or not. By default Image Management would be disabled.  **_Since_** Horizon 7.10  


  * This property has a default value of false.
* This property need not be set.
* This property cannot be updated.

  
**cloudManaged**|  xsd:boolean|  Indicates whether this cluster/pod is managed by Horizon Cloud Services for Broker.Next use case. This can be set to false, only when there are no cloud managed desktops.  **_Since_** Horizon 7.11  


  * This property has a default value of false.
* This property need not be set.

  
  
  
   
  
  
