---
layout: page
title: Data Object - ApplicationOtherFileTypeData
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Application.OtherFileTypeData`

Property of
> [ApplicationExecutionData](vdi.resources.Application.ApplicationExecutionData.md#field_detail)

Since
> Horizon 7.0


## Data Object Description

Information about different type of file types supported by Application that can be passed from agent to client via broker.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**type**|  xsd:string|  Type of the OtherFileType currently supported. Other types can be added in future. Examples ApplicationConstants.OtherFileType.URL [^20]
**name**|  xsd:string|  The name for OtherFileType data. For eg. An object of OtheFileTypeData with type URL can have names http, https or skype. [^20]
**description**|  xsd:string|  Friendly name for the other file type - for example, "Http Web URL". If unset, no friendly name will be displayed. [^1] [^13]


 


[^1]: This property need not be set.
[^13]: This property has a maximum length of 1024 characters.
[^20]: This property cannot contain ? characters.