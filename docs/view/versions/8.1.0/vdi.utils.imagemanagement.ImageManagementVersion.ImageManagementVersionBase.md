---
layout: page
title: Data Object - ImageManagementVersionBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionBase  
Property of
     [ImageManagementVersionInfo](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionInfo.md#field_detail)  
Parameter to
     [ImageManagementVersion_CreateVersions](vdi.utils.imagemanagement.ImageManagementVersion.md#createVersions)  
See also
     [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [MapEntry](vdi.util.MapEntry.md)  
Since 
    Horizon 7.10

## Data Object Description 

Basic data about an Image Management Version. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The version name is the unique name used to identify this version.   


  * This property must contain only alphanumerics, dot, underscores, and dashes. The maximum length is 64 characters. 

  
**description**|  xsd:string|  The description is a set of notes about the version.   


* This property need not be set.
  * This property has a maximum length of 1024 characters. 

  
**status**|  xsd:string|  Image management version status.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"AVAILABLE"| Image management version is available for pools to be created.  
"DEPLOYING_VM"| Image management version is deploying VM on the selected pod.  
"DEPLOYMENT_DONE"| Image management version status when VM deployment is done for the selected pod.  
"DELETED"| Image management version has been deleted.  
"DISABLED"| Image management version has been disabled and no further pool operation can be done using the same.  
"FAILED"| Image management version creation has failed.  
"PARTIALLY_AVAILABLE"| Some of the image management asset creation in some of the virtual centers have failed.  
"PUBLISHING"| Image management version is being published and specialized internally like installing agents etc..  
"REPLICATING"| Copying the specialized images across all virtual centers.  

  
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Image management stream id for this image version   


* This property cannot be updated.

  
**additionalDetails**| [MapEntry[]](vdi.util.MapEntry.md)|  Additional details about image management version.   


* This property need not be set.

  
  
  
  
  
  

