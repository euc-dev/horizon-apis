---
layout: page
title: Data Object - BaseImageVmIncompatibleReasons
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.BaseImageVm.BaseImageVmIncompatibleReasons  
Property of
     [BaseImageVmInfo](vdi.utils.virtualcenter.BaseImageVm.BaseImageVmInfo.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Reasons that may preclude this BaseImageVm from having its snapshots used in linked or instant clone desktop or farm creation. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**inUseByDesktop**|  xsd:boolean|  This BaseImageVm is already a machine that belongs to another manual or automatic desktop or farm. If true, this cannot be used in linked or instant clone desktop or farm creation.   


* This property cannot be updated.

  
**inUseByLinkedCloneDesktop**|  xsd:boolean|  This BaseImageVm is already a machine that belongs to a linked clone desktop or farm. If true, this cannot be used in linked or instant clone desktop or farm creation.   


* This property cannot be updated.

  
**viewComposerReplica**|  xsd:boolean|  This BaseImageVm is a View Composer or Instant Clone Engine replica. If true, this cannot be used in linked or instant clone desktop or farm creation.   


* This property cannot be updated.

  
**unsupportedOSForLinkedCloneFarm**|  xsd:boolean|  This BaseImageVm has a supported OS but contains no snapshots. If true, this cannot be used in linked or instant clone or farm creation.  **_Since_** Horizon View 6.2  


* This property cannot be updated.

  
**unsupportedOS**|  xsd:boolean|  This BaseImageVm has an unsupported desktop operating system. Certain desktop server operating systems are only supported when [enableServerInSingleUserMode](vdi.infrastructure.GlobalSettings.GeneralData.md#enableServerInSingleUserMode) is enabled. If true, this cannot be used in linked or instant clone desktop creation.   


* This property cannot be updated.

  
**noSnapshots**|  xsd:boolean|  This BaseImageVm has a supported OS but contains no snapshots. If true, this cannot be used in linked or instant clone desktop or farm creation.   


* This property cannot be updated.

  
**instantInternal**|  xsd:boolean|  This BaseImageVm is a Instant Clone Engine internal virtual machine. If true, this cannot be used in instant clone desktop or farm creation. When this is true, [viewComposerReplica](vdi.utils.virtualcenter.BaseImageVm.BaseImageVmIncompatibleReasons.md#viewComposerReplica) is also true for retaining backward compatibility.  **_Since_** Horizon 7.6  


  * This property has a default value of false.
* This property cannot be updated.

  
**inUseByInstantCloneDesktop**|  xsd:boolean|  This BaseImageVm is already a machine that belongs to a instant clone desktop or farm. If true, this cannot be used in linked or instant clone desktop or farm creation.  **_Since_** Horizon 8.0  


  * This property has a default value of false.
* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

