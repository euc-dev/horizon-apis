---
layout: page
title: Data Object - VmFolderIncompatibleReasons
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.VmFolder.VmFolderIncompatibleReasons`

Property of
> [VmFolderData](vdi.utils.virtualcenter.VmFolder.VmFolderData.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Reasons that may preclude this VM folder from being used in desktop creation.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**inUse**|  xsd:boolean|  Whether or not the VM folder is in use by another desktop. If true, this VM folder cannot be used in desktop creation. [^2]
**viewComposerReplicaFolder**|  xsd:boolean|  Whether or not the VM folder currently holds View Composer or Instant Clone Engine replicas. If true, this VM folder cannot be used in linked or instant clone desktop creation. [^2]
 


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.