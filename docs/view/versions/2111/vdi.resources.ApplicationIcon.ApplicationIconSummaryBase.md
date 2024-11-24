---
layout: page
title: Data Object - ApplicationIconSummaryBase
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.ApplicationIcon.ApplicationIconSummaryBase`

Property of
> [ApplicationIconSummaryView](vdi.resources.ApplicationIcon.ApplicationIconSummaryView.md#field_detail)

Since
> Horizon 7.5


## Data Object Description

Application Summary base that represents the metadata of the application icon.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**width**|  xsd:long|  Icon width
**height**|  xsd:long|  Icon height
**iconHash**|  xsd:string|  Icon hash, to enable quick icon lookup
**iconSource**|  xsd:string|  Source of the ApplicationIcon. If icon is from RDS Agent, iconSource will be Unset. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"BROKER"</td><td>supported ApplicationIcon sources</td></tr></table>


 


[^1]: This property need not be set.