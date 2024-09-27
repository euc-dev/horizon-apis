---
layout: page
title: Data Object - FarmAutomatedFarmData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.AutomatedFarmData  
Property of
     [FarmInfo](vdi.resources.Farm.FarmInfo.md#field_detail)  
See also
     [FarmCustomizationSettings](vdi.resources.Farm.CustomizationSettings.md), [FarmProvisioningStatusData](vdi.resources.Farm.ProvisioningStatusData.md), [FarmRDSServerMaxSessionsData](vdi.resources.Farm.RDSServerMaxSessionsData.md), [FarmRDSServerNamingSettings](vdi.resources.Farm.RDSServerNamingSettings.md), [FarmVirtualCenterManagedCommonSettings](vdi.resources.Farm.VirtualCenterManagedCommonSettings.md), [FarmVirtualCenterNamesData](vdi.resources.Farm.VirtualCenterNamesData.md), [FarmVirtualCenterProvisioningSettings](vdi.resources.Farm.VirtualCenterProvisioningSettings.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)  
Since 
    Horizon View 6.2

## Data Object Description 

Data for an automated farm. An automated farm is a pool that contains one or more dynamically generated RDS Servers that are automatically created and customized by View Manager from a Virtual Center virtual machine's snapshot. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**provisioningType**|  xsd:string|  The Source or the Provisioning Type of RDS Servers.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIEW_COMPOSER"| View composer linked clones managed as view RDS Servers. They share the same base image and use less storage space than full RDS Servers.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view RDS Servers. Instant clone engine uses vmfork technology to create the instant clones, these clones take much less time for provisioning. Instant clones have many similarities to linked clones like :-  

    * Both instant and linked clones share the same base image and use less storage space than full virtual machines.
    * The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
This option is only valid for Automated Farm.  

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center server.   


* This property cannot be updated.

  
**rdsServerNamingSettings**| [FarmRDSServerNamingSettings](vdi.resources.Farm.RDSServerNamingSettings.md)|  Specifies the naming scheme for the RDS Servers in the automated farm.   
  
**virtualCenterProvisioningSettings**| [FarmVirtualCenterProvisioningSettings](vdi.resources.Farm.VirtualCenterProvisioningSettings.md)|  Virtual Center provisioning settings for the automated farm.   
  
**virtualCenterManagedCommonSettings**| [FarmVirtualCenterManagedCommonSettings](vdi.resources.Farm.VirtualCenterManagedCommonSettings.md)|  Common settings for RDS Servers managed by Virtual Center sources.   
  
**virtualCenterNamesData**| [FarmVirtualCenterNamesData](vdi.resources.Farm.VirtualCenterNamesData.md)|  Naming data for Virtual Center entities associated with this automated farm.   


* This property cannot be updated.

  
**provisioningStatusData**| [FarmProvisioningStatusData](vdi.resources.Farm.ProvisioningStatusData.md)|  Provisioning status data about this automated farm.   


* This property cannot be updated.

  
**customizationSettings**| [FarmCustomizationSettings](vdi.resources.Farm.CustomizationSettings.md)|  Customization settings for this automated farm.   
  
**rdsServerMaxSessionsData**| [FarmRDSServerMaxSessionsData](vdi.resources.Farm.RDSServerMaxSessionsData.md)|  RDS Server max sessions data   
  
  
  
  
  
  

