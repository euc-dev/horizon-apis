---
layout: page
title: Data Object - ApplicationExecutionData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Application.ApplicationExecutionData`

Property of
> [ApplicationDiscoveryData](vdi.resources.Application.ApplicationDiscoveryData.md#field_detail), [ApplicationInfo](vdi.resources.Application.ApplicationInfo.md#field_detail), [ApplicationSpec](vdi.resources.Application.ApplicationSpec.md#field_detail)

See also
> [ApplicationFileTypeData](vdi.resources.Application.FileTypeData.md), [ApplicationOtherFileTypeData](vdi.resources.Application.OtherFileTypeData.md), [DesktopId](vdi.entity.DesktopId.md), [FarmId](vdi.entity.FarmId.md)

Since
> Horizon View 6.0


## Data Object Description

Application execution data needed to create/update an Application. Some of this information is obtained from Broker when the Application is discovered.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**executablePath**|  xsd:string|  Path to Application executable
**version**|  xsd:string|  Application version [^1]
**publisher**|  xsd:string|  Application publisher [^1]
**startFolder**|  xsd:string|  Starting folder for Application [^1]
**args**|  xsd:string|  parameters to pass to application when launching [^1]
**farm**| [FarmId](vdi.entity.FarmId.md)|  Farm Entity ID. It is marked as read-only because, once an Application is created with a FarmId, it is always associated with that Farm, and cannot be removed from the Farm, or added to another Farm. Either this or [desktop](vdi.resources.Application.ApplicationExecutionData.md#desktop) should be set. [^1] [^2]
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop Entity ID. It is marked as read-only because, once an Application is created with a desktopId, it is always associated with that Desktop, and cannot be removed from the Desktop, or added to another Desktop. Either this or [farm](vdi.resources.Application.ApplicationExecutionData.md#farm) should be set.  **_Since_** Horizon 7.9 [^1] [^2]
**fileTypes**| [ApplicationFileTypeData[]](vdi.resources.Application.FileTypeData.md)|  If set, set of file types reported by the application as supported (if this application is discovered) or as specified by the administrator (if this application is manually configured). If unset, this application does not present any file type support.  **_Since_** Horizon View 6.1 [^1] [^14]
**autoUpdateFileTypes**|  xsd:boolean|  Whether or not the file types supported by this application should be allowed to automatically update to reflect changes reported by the agent. Typically this should be set to false if the application has manually configured supported file types.  **_Since_** Horizon View 6.2 [^6]
**otherFileTypes**| [ApplicationOtherFileTypeData[]](vdi.resources.Application.OtherFileTypeData.md)|  If set, set of different type of file types reported by Application that can be passed from agent to client via broker or as specified by the administrator (if this application is manually configured). If unset, this application does not present any other file type support.  **_Since_** Horizon 7.0 [^1] [^14]
**autoUpdateOtherFileTypes**|  xsd:boolean|  Whether or not the other file types supported by this application should be allowed to automatically update to reflect changes reported by the agent. Typically this should be set to false if the application has manually configured supported file types.  **_Since_** Horizon 7.0 [^6]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^6]: This property has a default value of true.
[^14]: This property is an unordered array of unique values.