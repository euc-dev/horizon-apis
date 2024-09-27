---
layout: page
title: Data Object - VmFolderData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VmFolder.VmFolderData  
Property of
     [VmFolderInfo](vdi.utils.virtualcenter.VmFolder.VmFolderInfo.md#field_detail)  
See also
     [DatacenterId](vdi.entity.DatacenterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VmFolderIncompatibleReasons](vdi.utils.virtualcenter.VmFolder.VmFolderIncompatibleReasons.md)  
Since 
    Horizon View 6.0

## Data Object Description 

VmFolderData is a set of attributes for a folder retrieved from the VC. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  VM folder display name   


* This property cannot be updated.

  
**path**|  xsd:string|  VM folder path   


* This property cannot be updated.

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this VM folder.   


* This property cannot be updated.

  
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this VM folder.   


* This property need not be set.
* This property cannot be updated.

  
**type**|  xsd:string|  The type of this VM folder node. Some types may not be suitable for desktop creation.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"DATACENTER"| A datacenter that serves as a folder suitable for use in desktop creation.  
"FOLDER"| A regular folder suitable for use in desktop creation.  
"OTHER"| Some other resource type that cannot be used in desktop creation.  

  
**incompatibleReasons**| [VmFolderIncompatibleReasons](vdi.utils.virtualcenter.VmFolder.VmFolderIncompatibleReasons.md)|  Reasons that may preclude this VM folder from being used in desktop creation.   


* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

