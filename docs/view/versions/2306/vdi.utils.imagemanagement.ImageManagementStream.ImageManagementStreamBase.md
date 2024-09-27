---
layout: page
title: Data Object - ImageManagementStreamBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamBase  
Property of
     [ImageManagementStreamInfo](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamInfo.md#field_detail)  
Parameter to
     [ImageManagementStream_CreateStreams](vdi.utils.imagemanagement.ImageManagementStream.md#createStreams)  
See also
     [MapEntry](vdi.util.MapEntry.md)  
Since 
    Horizon 7.10

## Data Object Description 

Basic data about an Image Management Stream. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The stream name is the unique name used to identify this stream.   


  * This property must contain only alphanumerics, underscores and dashes. The maximum length is 64 characters. 

  
**description**|  xsd:string|  The description is a set of notes about the stream.   


* This property need not be set.
  * This property has a maximum length of 1024 characters. 

  
**operatingSystem**|  xsd:string|  The guest operating system.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"Unknown"|   
"Windows XP"| Windows XP  
"Windows Vista"| Windows Vista  
"Windows 7"| Windows 7  
"Windows 8"| Windows 8  
"Windows 10"| Windows 10  
"Windows 11"| Windows 11  
"Windows Server 2003"| Windows Server 2003  
"Windows Server 2008"| Windows Server 2008  
"Windows Server 2008R2"| Windows Server 2008R2  
"Windows Server 2012"| Windows Server 2012  
"Windows Server 2012R2"| Windows Server 2012R2  
"Windows Server 10"| null  
"Windows Server 2016"| null  
"Windows Server 2016 or above"| Windows Server 2016 or above  
"Linux (other)"| Linux (other)  
"Linux Server (other)"| Linux server (other)  
"Linux (Ubuntu)"| Linux (Ubuntu)  
"Linux (Red Hat Enterprise Linux)"| Linux (Red Hat Enterprise)  
"Linux (SUSE Linux Enterprise Server)"| Linux (Suse)  
"Linux (CentOS)"| Linux (CentOS)  

  
**status**|  xsd:string|  Image management stream status.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"AVAILABLE"| Image management stream is available for pools/farms to be created.  
"DELETED"| Image management stream is deleted.  
"DISABLED"| Image management stream is disabled and no further pools/farms can be created using the same.  
"FAILED"| Image management stream creation has failed.  
"IN_PROGRESS"| Image management stream creation is in progress.  
"PARTIALLY_AVAILABLE"| Image management version could not be created in one or more environments.  
"PENDING"| Image management stream is in pending state to be created by a task.  

  
**source**|  xsd:string|  Source of image management stream.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"MARKET_PLACE"| Image management stream is from market place.  
"UPLOADED"| Image management stream is uploaded.  
"COPIED_FROM_STREAM"| Image management stream is copied from another stream.  
"COPIED_FROM_VERSION"| Image management stream is copied from a version.  

  
**publisher**|  xsd:string|  Image management stream publisher.   


* This property need not be set.

  
**additionalDetails**| [MapEntry[]](vdi.util.MapEntry.md)|  Additional details about image management stream.   


* This property need not be set.

  
**tagAvailable**|  xsd:boolean|  This will be set to true when: 

  * Image management stream is in AVAILABLE or PARTIALLY_AVAILABLE state
  * There is at least one image management version in AVAILABLE or PARTIALLY_AVAILABLE state for this stream
  * There is at least one image management tag associated with the image management version.

For a specific VirtualCenterId, image management tag information will be retrieved   


* This property need not be set.
* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

