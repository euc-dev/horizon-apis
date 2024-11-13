---
layout: page
title: Data Object - FarmProvisioningStatusData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.ProvisioningStatusData`

Property of
> [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md#field_detail)

See also
> [FarmInstantCloneProvisioningStatusData](vdi.resources.Farm.InstantCloneProvisioningStatusData.md)

Since
> Horizon View 6.2


## Data Object Description

Provisioning status data about this Automated Farm.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**lastProvisioningError**|  xsd:string|  String message detailing the last provisioning error on this automated farm while [stopProvisioningOnError](vdi.resources.Farm.VirtualCenterProvisioningSettings.md#stopProvisioningOnError) is enabled. This will be cleared when [enableProvisioning](vdi.resources.Farm.VirtualCenterProvisioningSettings.md#enableProvisioning) is updated to true. [^1] [^2]
**lastProvisioningErrorTime**|  xsd:dateTime|  Time the last provisioning error occurred on this automated farm while [stopProvisioningOnError](vdi.resources.Farm.VirtualCenterProvisioningSettings.md#stopProvisioningOnError) is enabled. This will be cleared when [enableProvisioning](vdi.resources.Farm.VirtualCenterProvisioningSettings.md#enableProvisioning) is updated to true. [^1] [^2]
**instantCloneProvisioningStatusData**| [FarmInstantCloneProvisioningStatusData](vdi.resources.Farm.InstantCloneProvisioningStatusData.md)|  ProvisioningStatusData applicable only to instant clone farms.  **_Since_** Horizon 7.1 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.