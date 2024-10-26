---
layout: page
title: Data Object - FarmAutomatedFarmData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.AutomatedFarmData`

Property of
> [FarmInfo](vdi.resources.Farm.FarmInfo.md#field_detail)

See also
> [FarmCustomizationSettings](vdi.resources.Farm.CustomizationSettings.md), [FarmProvisioningStatusData](vdi.resources.Farm.ProvisioningStatusData.md), [FarmRDSServerMaxSessionsData](vdi.resources.Farm.RDSServerMaxSessionsData.md), [FarmRDSServerNamingSettings](vdi.resources.Farm.RDSServerNamingSettings.md), [FarmVirtualCenterManagedCommonSettings](vdi.resources.Farm.VirtualCenterManagedCommonSettings.md), [FarmVirtualCenterNamesData](vdi.resources.Farm.VirtualCenterNamesData.md), [FarmVirtualCenterProvisioningSettings](vdi.resources.Farm.VirtualCenterProvisioningSettings.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.2


## Data Object Description

Data for an automated farm. An automated farm is a pool that contains one or more dynamically generated RDS Servers that are automatically created and customized by View Manager from a Virtual Center virtual machine's snapshot.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**provisioningType**|  xsd:string|  The Source or the Provisioning Type of RDS Servers. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIEW_COMPOSER</td><td>View composer linked clones managed as view RDS Servers. They share the same base image and use less storage space than full RDS Servers.</td></tr><tr><td>INSTANT_CLONE_ENGINE</td><td>Instant clone engine created 'instant clones' managed as view RDS Servers. Instant clone engine uses vmfork technology to create the instant clones, these clones take much less time for provisioning. Instant clones have many similarities to linked clones like :- [^109] [^110] This option is only valid for Automated Farm.</td></tr></table>
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center server. [^2]
**rdsServerNamingSettings**| [FarmRDSServerNamingSettings](vdi.resources.Farm.RDSServerNamingSettings.md)|  Specifies the naming scheme for the RDS Servers in the automated farm.
**virtualCenterProvisioningSettings**| [FarmVirtualCenterProvisioningSettings](vdi.resources.Farm.VirtualCenterProvisioningSettings.md)|  Virtual Center provisioning settings for the automated farm.
**virtualCenterManagedCommonSettings**| [FarmVirtualCenterManagedCommonSettings](vdi.resources.Farm.VirtualCenterManagedCommonSettings.md)|  Common settings for RDS Servers managed by Virtual Center sources.
**virtualCenterNamesData**| [FarmVirtualCenterNamesData](vdi.resources.Farm.VirtualCenterNamesData.md)|  Naming data for Virtual Center entities associated with this automated farm. [^2]
**provisioningStatusData**| [FarmProvisioningStatusData](vdi.resources.Farm.ProvisioningStatusData.md)|  Provisioning status data about this automated farm. [^2]
**customizationSettings**| [FarmCustomizationSettings](vdi.resources.Farm.CustomizationSettings.md)|  Customization settings for this automated farm.
**rdsServerMaxSessionsData**| [FarmRDSServerMaxSessionsData](vdi.resources.Farm.RDSServerMaxSessionsData.md)|  RDS Server max sessions data


 
