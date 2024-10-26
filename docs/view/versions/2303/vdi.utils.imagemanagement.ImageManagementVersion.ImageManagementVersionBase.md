---
layout: page
title: Data Object - ImageManagementVersionBase
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionBase`

Property of
> [ImageManagementVersionInfo](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionInfo.md#field_detail)

Parameter to
> [ImageManagementVersion_CreateVersions](vdi.utils.imagemanagement.ImageManagementVersion.md#createVersions)

See also
> [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon 7.10


## Data Object Description

Basic data about an Image Management Version.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  The version name is the unique name used to identify this version. [^150]
**description**|  xsd:string|  The description is a set of notes about the version. [^1] [^13]
**status**|  xsd:string|  Image management version status. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AVAILABLE</td><td>Image management version is available for pools to be created.</td></tr><tr><td>DEPLOYING_VM</td><td>Image management version is deploying VM on the selected pod.</td></tr><tr><td>DEPLOYMENT_DONE</td><td>Image management version status when VM deployment is done for the selected pod.</td></tr><tr><td>DELETED</td><td>Image management version has been deleted.</td></tr><tr><td>DISABLED</td><td>Image management version has been disabled and no further pool operation can be done using the same.</td></tr><tr><td>FAILED</td><td>Image management version creation has failed.</td></tr><tr><td>PARTIALLY_AVAILABLE</td><td>Some of the image management asset creation in some of the virtual centers have failed.</td></tr><tr><td>PUBLISHING</td><td>Image management version is being published and specialized internally like installing agents etc.</td></tr><tr><td>REPLICATING</td><td>Copying the specialized images across all virtual centers.</td></tr></table>
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Image management stream id for this image version [^2]
**additionalDetails**| [MapEntry[]](vdi.util.MapEntry.md)|  Additional details about image management version. [^1]
 


 
