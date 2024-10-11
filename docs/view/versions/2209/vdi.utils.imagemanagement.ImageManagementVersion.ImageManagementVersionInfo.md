---
layout: page
title: Data Object - ImageManagementVersionInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionInfo`

Returned by  
> [ImageManagementVersion_Get](vdi.utils.imagemanagement.ImageManagementVersion.md#get), [ImageManagementVersion_ListByImageManagementStream](vdi.utils.imagemanagement.ImageManagementVersion.md#listByImageManagementStream)

See also  
> [ImageManagementVersionBase](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionBase.md), [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)

Since  
> Horizon 7.10


## Data Object Description 

Top level object describing a image management version. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)|  Entity id image management version.   


* This property cannot be updated.

  
**base**| [ImageManagementVersionBase](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionBase.md)|  Basic data about a image management version.   
  
**refId**|  xsd:string|  Reference ID used for this image management version.  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.

  
  
  
 
  
  
