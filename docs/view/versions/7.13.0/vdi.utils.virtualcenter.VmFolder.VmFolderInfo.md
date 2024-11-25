---
layout: page
title: Data Object - VmFolderInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.VmFolder.VmFolderInfo`

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
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [VmFolderId](vdi.entity.VmFolderId.md)|  VmFolder Id [^2]
**folderData**| [VmFolderData](vdi.utils.virtualcenter.VmFolder.VmFolderData.md)|  Folder display data [^2]
**children**| [VmFolderInfo[]](vdi.utils.virtualcenter.VmFolder.VmFolderInfo.md)|  Children nodes of the tree-structure [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.