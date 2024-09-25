---
layout: page
title: Data Object - VmFolderInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VmFolder.VmFolderInfo
Property of
     [VmFolderInfo](vdi.utils.virtualcenter.VmFolder.VmFolderInfo.md#field_detail)
Returned by
     [VmFolder_GetVmFolderTree](vdi.utils.virtualcenter.VmFolder.md#getVmFolderTree)
See also
     [VmFolderData](vdi.utils.virtualcenter.VmFolder.VmFolderData.md), [VmFolderId](vdi.entity.VmFolderId.md), 
Since 
    Horizon View 6.0

## Data Object Description 

VmFolderInfo aggregates VmFolderData with FolderId for folders retrieved from the VC. It is a tree-structure. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [VmFolderId](vdi.entity.VmFolderId.md)|  VmFolder Id   


[^2]

  
**folderData**| [VmFolderData](vdi.utils.virtualcenter.VmFolder.VmFolderData.md)|  Folder display data   


[^2]

  
**children**| [VmFolderInfo[]](vdi.utils.virtualcenter.VmFolder.VmFolderInfo.md)|  Children nodes of the tree-structure   


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
