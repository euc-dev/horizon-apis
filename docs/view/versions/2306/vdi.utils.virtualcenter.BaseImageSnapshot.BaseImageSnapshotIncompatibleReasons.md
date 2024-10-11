---
layout: page
title: Data Object - BaseImageSnapshotIncompatibleReasons
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotIncompatibleReasons`

Property of  
> [BaseImageSnapshotInfo](vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotInfo.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

Reasons that may preclude this BaseImageSnapshot from being used in linked or instant clone desktop creation. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**poweredOn**|  xsd:boolean|  This BaseImageSnapshot is powered on. If true, this cannot be used in linked or instant clone desktop or farm creation.   


* This property cannot be updated.

  
**incompatibleInstantCloneVmHwVersion**|  xsd:boolean|  This value is true if the [hardwareVersion](vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotInfo.md#hardwareVersion) is not 11 or above. If true, this VM cannot be used in Instant clone desktop pool creation.  **_Since_** Horizon 7.0  


* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
