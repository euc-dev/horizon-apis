---
layout: page
title: Data Object - BaseImageVmInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.BaseImageVm.BaseImageVmInfo  
Returned by
     [BaseImageVm_Get](vdi.utils.virtualcenter.BaseImageVm.md#get), [BaseImageVm_List](vdi.utils.virtualcenter.BaseImageVm.md#list), [BaseImageVm_ListByDatacenter](vdi.utils.virtualcenter.BaseImageVm.md#listByDatacenter)  
See also
     [BaseImageVmId](vdi.entity.BaseImageVmId.md), [BaseImageVmIncompatibleReasons](vdi.utils.virtualcenter.BaseImageVm.BaseImageVmIncompatibleReasons.md), [DatacenterId](vdi.entity.DatacenterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

VMInfo is a set of VM attributes for parent VMs retrieved from the VC. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  VM id   


* This property cannot be updated.

  
**name**|  xsd:string|  VM name   


* This property cannot be updated.

  
**path**|  xsd:string|  VM path   


* This property cannot be updated.

  
**operatingSystem**|  xsd:string|  Operating system enumeration as known to View.   


* This property need not be set.
* This property cannot be updated.
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

  
**operatingSystemDisplayName**|  xsd:string|  Operating system display name from Virtual Center.   


* This property need not be set.
* This property cannot be updated.

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this VM   


* This property cannot be updated.

  
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this VM   


* This property need not be set.
* This property cannot be updated.

  
**incompatibleReasons**| [BaseImageVmIncompatibleReasons](vdi.utils.virtualcenter.BaseImageVm.BaseImageVmIncompatibleReasons.md)|  Reasons that may preclude this BaseImageVm from having its snapshots used in linked clone desktop or farm creation.   


* This property cannot be updated.

  
**networkType**|  xsd:string|  Type of network base image vm belongs to.  **_Since_** Horizon 7.9  


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"Network"| Standard network  
"OpaqueNetwork"| Opaque network  
"DistributedVirtualPortgroup"| DVS port group  

  
**refId**|  xsd:string|  Reference ID used for this base image VM.  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.

  
  
  

  
  

