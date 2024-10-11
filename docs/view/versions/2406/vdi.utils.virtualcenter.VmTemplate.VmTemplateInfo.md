---
layout: page
title: Data Object - VmTemplateInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VmTemplate.VmTemplateInfo`

Returned by  
> [VmTemplate_List](vdi.utils.virtualcenter.VmTemplate.md#list), [VmTemplate_ListByDatacenter](vdi.utils.virtualcenter.VmTemplate.md#listByDatacenter)

See also  
> [DatacenterId](vdi.entity.DatacenterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VmTemplateId](vdi.entity.VmTemplateId.md), [VmTemplateIncompatibleReasons](vdi.utils.virtualcenter.VmTemplate.VmTemplateIncompatibleReasons.md)

Since  
> Horizon View 6.0


## Data Object Description 

VMTemplateInfo is a set of template attributes retrieved from the VC. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [VmTemplateId](vdi.entity.VmTemplateId.md)|  VM template Id   


 * This property cannot be updated.

  
**name**|  xsd:string|  VM template name   


 * This property cannot be updated.

  
**path**|  xsd:string|  VM template path   


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
"Windows 11"| Windows 11  
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

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this template   


 * This property cannot be updated.

  
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this template   


 * This property need not be set.
 * This property cannot be updated.

  
**hardwareVersion**|  xsd:int|  Template hardware version.   


 * This property need not be set.
 * This property cannot be updated.

  
**vGPUType**|  xsd:string|  NVIDIA GRID vGPU type configured on this template, if any.  **_Since_** Horizon View 6.1  


 * This property need not be set.
 * This property cannot be updated.

  
**incompatibleReasons**| [VmTemplateIncompatibleReasons](vdi.utils.virtualcenter.VmTemplate.VmTemplateIncompatibleReasons.md)|  Reasons that may preclude this VmTemplate from being used in full clone desktop creation.   


 * This property cannot be updated.

  
**memoryMB**|  xsd:int|  Memory size of the template, in MB.  **_Since_** Horizon 7.4  


 * This property need not be set.
 * This property cannot be updated.

  
**diskSizeInBytes**|  xsd:long|  Sum of capacities of all the virtual disks in the template, in bytes.  **_Since_** Horizon 7.4  


 * This property need not be set.
 * This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this vm template.  **_Since_** Horizon 8.1  


 * This property need not be set.
 * This property cannot be updated.

  
  

  
