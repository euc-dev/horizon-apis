---
layout: page
title: Data Object - FarmAutomatedFarmSpec
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.AutomatedFarmSpec`

Property of
> [FarmSpec](vdi.resources.Farm.FarmSpec.md#field_detail)

See also
> [FarmCustomizationSettings](vdi.resources.Farm.CustomizationSettings.md), [FarmRDSServerMaxSessionsData](vdi.resources.Farm.RDSServerMaxSessionsData.md), [FarmRDSServerNamingSpec](vdi.resources.Farm.RDSServerNamingSpec.md), [FarmVirtualCenterManagedCommonSettings](vdi.resources.Farm.VirtualCenterManagedCommonSettings.md), [FarmVirtualCenterProvisioningSettings](vdi.resources.Farm.VirtualCenterProvisioningSettings.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.2


## Data Object Description

Specification for an automated farm. An automated farm is a pool that contains one or more dynamically generated RDS Servers that are automatically created and customized by View Manager from a Virtual Center virtual machine's snapshot.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**provisioningType**|  xsd:string|  The Source or the Provisioning Type of RDS Servers. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIEW_COMPOSER</td><td>View composer linked clones managed as view RDS Servers. They share the same base image and use less storage space than full RDS Servers.</td></tr><tr><td>INSTANT_CLONE_ENGINE</td><td>Instant clone engine created 'instant clones' managed as view RDS Servers. Instant clone engine uses vmfork technology to create the instant clones, these clones take much less time for provisioning. Instant clones have many similarities to linked clones like :- [^109] [^110] This option is only valid for Automated Farm.</td></tr></table>
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center server.
**rdsServerNamingSpec**| [FarmRDSServerNamingSpec](vdi.resources.Farm.RDSServerNamingSpec.md)|  Specifies the naming scheme for the RDS Servers in the farm.
**virtualCenterProvisioningSettings**| [FarmVirtualCenterProvisioningSettings](vdi.resources.Farm.VirtualCenterProvisioningSettings.md)|  Virtual Center provisioning settings for the automated farm.
**virtualCenterManagedCommonSettings**| [FarmVirtualCenterManagedCommonSettings](vdi.resources.Farm.VirtualCenterManagedCommonSettings.md)|  Common settings for RDS Servers managed by Virtual Center sources.
**customizationSettings**| [FarmCustomizationSettings](vdi.resources.Farm.CustomizationSettings.md)|  Customization settings.
**rdsServerMaxSessionsData**| [FarmRDSServerMaxSessionsData](vdi.resources.Farm.RDSServerMaxSessionsData.md)|  RDS Server max sessions data
 


 


[^2]: This property cannot be updated.
[^109]: Both instant and linked clones share the same base image and use less storage space than full virtual machines.
[^110]: The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.