---
layout: page
title: Data Object - VmTemplateInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VmTemplate.VmTemplateInfo
Returned by
     [VmTemplate_List](vdi.utils.virtualcenter.VmTemplate.md#list), [VmTemplate_ListByDatacenter](vdi.utils.virtualcenter.VmTemplate.md#listByDatacenter)
See also
     [DatacenterId](vdi.entity.DatacenterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VmTemplateId](vdi.entity.VmTemplateId.md), [VmTemplateIncompatibleReasons](vdi.utils.virtualcenter.VmTemplate.VmTemplateIncompatibleReasons.md)
Since 
    Horizon View 6.0

## Data Object Description 

VMTemplateInfo is a set of template attributes retrieved from the VC. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [VmTemplateId](vdi.entity.VmTemplateId.md)|  VM template Id   


[^2]

  
**name**|  xsd:string|  VM template name   


[^2]

  
**path**|  xsd:string|  VM template path   


[^2]

  
**operatingSystem**|  xsd:string|  Operating system enumeration as known to View.   


[^1]
[^2]
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


[^1]
[^2]

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this template   


[^2]

  
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this template   


[^1]
[^2]

  
**hardwareVersion**|  xsd:int|  Template hardware version.   


[^1]
[^2]

  
**vGPUType**|  xsd:string|  NVIDIA GRID vGPU type configured on this template, if any.  **_Since_** Horizon View 6.1  


[^1]
[^2]

  
**incompatibleReasons**| [VmTemplateIncompatibleReasons](vdi.utils.virtualcenter.VmTemplate.VmTemplateIncompatibleReasons.md)|  Reasons that may preclude this VmTemplate from being used in full clone desktop creation.   


[^2]

  
**memoryMB**|  xsd:int|  Memory size of the template, in MB.  **_Since_** Horizon 7.4  


[^1]
[^2]

  
**diskSizeInBytes**|  xsd:long|  Sum of capacities of all the virtual disks in the template, in bytes.  **_Since_** Horizon 7.4  


[^1]
[^2]

  
**refId**|  xsd:string|  Reference ID used for this vm template.  **_Since_** Horizon 8.1  


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

