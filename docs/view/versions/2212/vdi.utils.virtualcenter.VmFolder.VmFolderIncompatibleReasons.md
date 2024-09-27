---
layout: page
title: Data Object - VmFolderIncompatibleReasons
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VmFolder.VmFolderIncompatibleReasons  
Property of
     [VmFolderData](vdi.utils.virtualcenter.VmFolder.VmFolderData.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Reasons that may preclude this VM folder from being used in desktop creation. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**inUse**|  xsd:boolean|  Whether or not the VM folder is in use by another desktop. If true, this VM folder cannot be used in desktop creation.   


* This property cannot be updated.

  
**viewComposerReplicaFolder**|  xsd:boolean|  Whether or not the VM folder currently holds View Composer or Instant Clone Engine replicas. If true, this VM folder cannot be used in linked or instant clone desktop creation.   


* This property cannot be updated.

  
  
  
  
  
  

