---
layout: page
title: Data Object - DesktopProvisioningView
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.DesktopProvisioningView`

See also  
> [DesktopBase](vdi.resources.Desktop.DesktopBase.md), [DesktopId](vdi.entity.DesktopId.md), [DesktopVirtualCenterData](vdi.resources.Desktop.VirtualCenterData.md)

Since  
> Horizon 7.10


## Data Object Description 

Virtual Center entities associated with the automated Desktop. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

The DesktopProvisioningView query service api to get provisioning data. 

  * [provisioningType](vdi.resources.Desktop.DesktopProvisioningView.md#provisioningType)
  * [base](vdi.resources.Desktop.DesktopProvisioningView.md#base).[name](vdi.resources.Desktop.DesktopBase.md#name)
  * [virtualCenterData](vdi.resources.Desktop.DesktopProvisioningView.md#virtualCenterData).[virtualCenter](vdi.resources.Desktop.VirtualCenterData.md#virtualCenter)
  * [virtualCenterData](vdi.resources.Desktop.DesktopProvisioningView.md#virtualCenterData).[imageManagementStream](vdi.resources.Desktop.VirtualCenterData.md#imageManagementStream)
  * [virtualCenterData](vdi.resources.Desktop.DesktopProvisioningView.md#virtualCenterData).[imageManagementTag](vdi.resources.Desktop.VirtualCenterData.md#imageManagementTag)
  * [virtualCenterData](vdi.resources.Desktop.DesktopProvisioningView.md#virtualCenterData).[pendingImageManagementStream](vdi.resources.Desktop.VirtualCenterData.md#pendingImageManagementStream)
  * [virtualCenterData](vdi.resources.Desktop.DesktopProvisioningView.md#virtualCenterData).[pendingImageManagementTag](vdi.resources.Desktop.VirtualCenterData.md#pendingImageManagementTag)



Query Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  This query will return results only for desktops the caller has desktop read privilege on with the corresponding access group permission.   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop entity ID.   


* This property cannot be updated.

  
**provisioningType**|  xsd:string|  The Source or the Provisioning Type of machines.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.  
"VIEW_COMPOSER"| View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones like :-  

    * Both instant and linked clones share the same base image and use less storage space than full virtual machines.
    * The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
This option is only valid for Automated Desktop.  

  
**operatingSystem**|  xsd:string|  The guest operating system.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"Unknown"|   
"Windows XP"| Windows XP  
"Windows Vista"| Windows Vista  
"Windows 7"| Windows 7  
"Windows 8"| Windows 8  
"Windows 10"| Windows 10  
"Windows Server 2003"| Windows Server 2003  
"Windows Server 2008"| Windows Server 2008  
"Windows Server 2008R2"| Windows Server 2008R2  
"Windows Server 2012"| Windows Server 2012  
"Windows Server 2012R2"| Windows Server 2012R2  
"Windows Server 10"| null  
"Windows Server 2016"| null  
"Windows Server 2016 or above"| Windows Server 2016 or above  
"Linux (other)"| Linux (other)  
"Linux Server (other)"| Linux server (other)  
"Linux (Ubuntu)"| Linux (Ubuntu)  
"Linux (Red Hat Enterprise Linux)"| Linux (Red Hat Enterprise)  
"Linux (SUSE Linux Enterprise Server)"| Linux (Suse)  
"Linux (CentOS)"| Linux (CentOS)  

  
**operatingSystemArchitecture**|  xsd:string|  The guest operating system architecture.   


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"Unknown"| Operating System cannot be determined.  
"32_bit"| 32 bit Operating System Architecture.  
"64_bit"| 64 bit Operating System Architecture.  

  
**base**| [DesktopBase](vdi.resources.Desktop.DesktopBase.md)|  Desktop identification information.   


* This property cannot be updated.

  
**virtualCenterData**| [DesktopVirtualCenterData](vdi.resources.Desktop.VirtualCenterData.md)|  Paths for Virtual Center entities associated with this Desktop.   


* This property cannot be updated.

  
  
  

  
  
