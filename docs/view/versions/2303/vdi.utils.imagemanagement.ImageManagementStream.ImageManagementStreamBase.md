---
layout: page
title: Data Object - ImageManagementStreamBase
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamBase`

Property of
> [ImageManagementStreamInfo](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamInfo.md#field_detail)

Parameter to
> [ImageManagementStream_CreateStreams](vdi.utils.imagemanagement.ImageManagementStream.md#createStreams)

See also
> [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon 7.10


## Data Object Description

Basic data about an Image Management Stream.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  The stream name is the unique name used to identify this stream. [^148]
**description**|  xsd:string|  The description is a set of notes about the stream. [^1] [^13]
**operatingSystem**|  xsd:string|  The guest operating system. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Unknown</td><td></td></tr><tr><td>Windows XP</td><td>Windows XP</td></tr><tr><td>Windows Vista</td><td>Windows Vista</td></tr><tr><td>Windows 7</td><td>Windows 7</td></tr><tr><td>Windows 8</td><td>Windows 8</td></tr><tr><td>Windows 10</td><td>Windows 10</td></tr><tr><td>Windows 11</td><td>Windows 11</td></tr><tr><td>Windows Server 2003</td><td>Windows Server 2003</td></tr><tr><td>Windows Server 2008</td><td>Windows Server 2008</td></tr><tr><td>Windows Server 2008R2</td><td>Windows Server 2008R2</td></tr><tr><td>Windows Server 2012</td><td>Windows Server 2012</td></tr><tr><td>Windows Server 2012R2</td><td>Windows Server 2012R2</td></tr><tr><td>Windows Server 10</td><td>null</td></tr><tr><td>Windows Server 2016</td><td>null</td></tr><tr><td>Windows Server 2016 or above</td><td>Windows Server 2016 or above</td></tr><tr><td>Linux (other)</td><td>Linux (other)</td></tr><tr><td>Linux Server (other)</td><td>Linux server (other)</td></tr><tr><td>Linux (Ubuntu)</td><td>Linux (Ubuntu)</td></tr><tr><td>Linux (Red Hat Enterprise Linux)</td><td>Linux (Red Hat Enterprise)</td></tr><tr><td>Linux (SUSE Linux Enterprise Server)</td><td>Linux (Suse)</td></tr><tr><td>Linux (CentOS)</td><td>Linux (CentOS)</td></tr></table>
**status**|  xsd:string|  Image management stream status. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AVAILABLE</td><td>Image management stream is available for pools/farms to be created.</td></tr><tr><td>DELETED</td><td>Image management stream is deleted.</td></tr><tr><td>DISABLED</td><td>Image management stream is disabled and no further pools/farms can be created using the same.</td></tr><tr><td>FAILED</td><td>Image management stream creation has failed.</td></tr><tr><td>IN_PROGRESS</td><td>Image management stream creation is in progress.</td></tr><tr><td>PARTIALLY_AVAILABLE</td><td>Image management version could not be created in one or more environments.</td></tr><tr><td>PENDING</td><td>Image management stream is in pending state to be created by a task.</td></tr></table>
**source**|  xsd:string|  Source of image management stream. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>MARKET_PLACE</td><td>Image management stream is from market place.</td></tr><tr><td>UPLOADED</td><td>Image management stream is uploaded.</td></tr><tr><td>COPIED_FROM_STREAM</td><td>Image management stream is copied from another stream.</td></tr><tr><td>COPIED_FROM_VERSION</td><td>Image management stream is copied from a version.</td></tr></table>
**publisher**|  xsd:string|  Image management stream publisher. [^1]
**additionalDetails**| [MapEntry[]](vdi.util.MapEntry.md)|  Additional details about image management stream. [^1]
**tagAvailable**|  xsd:boolean|  This will be set to true when: [^144] [^145] [^146]. <br>For a specific VirtualCenterId, image management tag information will be retrieved [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^13]: This property has a maximum length of 1024 characters.
[^144]: Image management stream is in AVAILABLE or PARTIALLY_AVAILABLE state.
[^145]: There is at least one image management version in AVAILABLE or PARTIALLY_AVAILABLE state for this stream.
[^146]: There is at least one image management tag associated with the image management version.
[^148]: This property must contain only alphanumerics, underscores and dashes. The maximum length is 64 characters.