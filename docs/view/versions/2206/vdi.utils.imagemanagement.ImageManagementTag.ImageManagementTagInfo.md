---
layout: page
title: Data Object - ImageManagementTagInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagInfo  
Returned by
     [ImageManagementTag_Get](vdi.utils.imagemanagement.ImageManagementTag.md#get), [ImageManagementTag_ListBySpec](vdi.utils.imagemanagement.ImageManagementTag.md#listBySpec)  
See also
     [ImageManagementTagBase](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagBase.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)  
Since 
    Horizon 7.10

## Data Object Description 

Top level object describing a image management tag. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Entity id image management tag.   


* This property cannot be updated.

  
**base**| [ImageManagementTagBase](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagBase.md)|  Basic data about a image management tag.   
  
**refId**|  xsd:string|  Reference ID used for this image management tag.  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.

  
  
  
 
  
  

