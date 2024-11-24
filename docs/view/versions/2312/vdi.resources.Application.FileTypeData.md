---
layout: page
title: Data Object - ApplicationFileTypeData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Application.FileTypeData`

Property of
> [ApplicationExecutionData](vdi.resources.Application.ApplicationExecutionData.md#field_detail)

Since
> Horizon View 6.1


## Data Object Description

Information about a file types supported by the application.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**fileType**|  xsd:string|  File type supported by this application. This value is case insensitive. If multiple file types are specified using the same (case insensitive) name and description, all but one will be ignored. [^181]
**description**|  xsd:string|  Friendly name for the file type - for example, "Microsoft Word document". If unset, no friendly name will be displayed. [^1] [^13]


 


[^1]: This property need not be set.
[^13]: This property has a maximum length of 1024 characters.
[^181]: This property cannot contain forward slashes.