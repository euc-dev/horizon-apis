---
layout: page
title: Data Object - FarmProvisioningView
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.FarmProvisioningView
See also
     [FarmBase](vdi.resources.Farm.FarmBase.md), [FarmId](vdi.entity.FarmId.md), [FarmVirtualCenterData](vdi.resources.Farm.VirtualCenterData.md)
Since 
    Horizon 7.10

## Data Object Description 

Virtual Center entities associated with this Automated Farm. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

The FarmProvisioningView query service api to get provisioning data. The fields which can be used in filters are: 

  * [provisioningType](vdi.resources.Farm.FarmProvisioningView.md#provisioningType)
  * [base](vdi.resources.Farm.FarmProvisioningView.md#base).[name](vdi.resources.Farm.FarmBase.md#name)
  * [virtualCenterData](vdi.resources.Farm.FarmProvisioningView.md#virtualCenterData).[virtualCenter](vdi.resources.Farm.VirtualCenterData.md#virtualCenter)
  * [virtualCenterData](vdi.resources.Farm.FarmProvisioningView.md#virtualCenterData).[imageManagementStream](vdi.resources.Farm.VirtualCenterData.md#imageManagementStream)
  * [virtualCenterData](vdi.resources.Farm.FarmProvisioningView.md#virtualCenterData).[imageManagementTag](vdi.resources.Farm.VirtualCenterData.md#imageManagementTag)
  * [virtualCenterData](vdi.resources.Farm.FarmProvisioningView.md#virtualCenterData).[pendingImageManagementStream](vdi.resources.Farm.VirtualCenterData.md#pendingImageManagementStream)
  * [virtualCenterData](vdi.resources.Farm.FarmProvisioningView.md#virtualCenterData).[pendingImageManagementTag](vdi.resources.Farm.VirtualCenterData.md#pendingImageManagementTag)



Query Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required to query Farm provisioning view.   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [FarmId](vdi.entity.FarmId.md)|  Farm entity ID   


[^2]

  
**provisioningType**|  xsd:string|  The Source or the Provisioning Type of RDS Servers.   


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIEW_COMPOSER"| View composer linked clones managed as view RDS Servers. They share the same base image and use less storage space than full RDS Servers.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view RDS Servers. Instant clone engine uses vmfork technology to create the instant clones, these clones take much less time for provisioning. Instant clones have many similarities to linked clones like :-  

    * Both instant and linked clones share the same base image and use less storage space than full virtual machines.
    * The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
This option is only valid for Automated Farm.  

  
**operatingSystem**|  xsd:string|  The guest operating system.   


[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"Unknown"|   
"Windows Server 2003"| Windows Server 2003  
"Windows Server 2008"| Windows Server 2008  
"Windows Server 2008R2"| Windows Server 2008R2  
"Windows Server 2012"| Windows Server 2012  
"Windows Server 2012R2"| Windows Server 2012R2  
"Windows Server 2016"| null  
"Linux Server (other)"| Linux server (other)  

  
**operatingSystemArchitecture**|  xsd:string|  The guest operating system architecture.   


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"Unknown"| Operating System cannot be determined.  
"32_bit"| 32 bit Operating System Architecture.  
"64_bit"| 64 bit Operating System Architecture.  

  
**base**| [FarmBase](vdi.resources.Farm.FarmBase.md)|  Farm identification information.   


[^2]

  
**virtualCenterData**| [FarmVirtualCenterData](vdi.resources.Farm.VirtualCenterData.md)|  Paths for Virtual Center entities associated with this Farm.   


[^2]

  
**refId**|  xsd:string|  Reference ID used for this farm.  **_Since_** Horizon 8.2  


[^1]
[^2]

  
  

  

