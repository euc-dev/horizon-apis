---
layout: page
title: Data Object - GlobalFeatureSettings
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.FeatureSettings`

Property of
> [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md#field_detail)

Returned by
> [GlobalSettings_GetFeatureSettings](vdi.infrastructure.GlobalSettings.md#getFeatureSettings)

Since
> Horizon 7.5


## Data Object Description

Feature settings.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**enableHelpdesk**|  xsd:boolean|  Determines whether help desk feature is enabled or not. By default enableHelpdesk is true and helpdesk would be enabled. [^6] [^1] [^2]
**enableImageManagement**|  xsd:boolean|  Determines whether Image Management feature is enabled or not. By default Image Management would be disabled.  **_Since_** Horizon 7.10 [^5] [^1] [^2]
**cloudManaged**|  xsd:boolean|  Indicates whether this cluster/pod is managed by Horizon Cloud Services for Broker.Next use case. This can be set to false, only when there are no cloud managed desktops.  **_Since_** Horizon 7.11 [^5] [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.