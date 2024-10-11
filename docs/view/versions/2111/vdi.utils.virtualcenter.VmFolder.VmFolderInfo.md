---
layout: page
title: Data Object - VmFolderInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VmFolder.VmFolderInfo`

Property of  
> [VmFolderInfo](vdi.utils.virtualcenter.VmFolder.VmFolderInfo.md#field_detail)

Returned by  
> [VmFolder_GetVmFolderTree](vdi.utils.virtualcenter.VmFolder.md#getVmFolderTree)

See also  
> [VmFolderData](vdi.utils.virtualcenter.VmFolder.VmFolderData.md), [VmFolderId](vdi.entity.VmFolderId.md),

Since  
> Horizon View 6.0


## Data Object Description 

VmFolderInfo aggregates VmFolderData with FolderId for folders retrieved from the VC. It is a tree-structure. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [VmFolderId](vdi.entity.VmFolderId.md)|  VmFolder Id   


* This property cannot be updated.

  
**folderData**| [VmFolderData](vdi.utils.virtualcenter.VmFolder.VmFolderData.md)|  Folder display data   


* This property cannot be updated.

  
**children**| [VmFolderInfo[]](vdi.utils.virtualcenter.VmFolder.VmFolderInfo.md)|  Children nodes of the tree-structure   


* This property need not be set.
* This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this vm folder.  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.

  
  
  
   
  
  
