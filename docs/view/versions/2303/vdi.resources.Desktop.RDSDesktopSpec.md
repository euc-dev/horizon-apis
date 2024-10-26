---
layout: page
title: Data Object - DesktopRDSDesktopSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.RDSDesktopSpec`

Property of
> [DesktopSpec](vdi.resources.Desktop.DesktopSpec.md#field_detail)

See also
> [FarmId](vdi.entity.FarmId.md)

Since
> Horizon View 6.0


## Data Object Description

Specification for a RDS Desktop. An RDS Desktop has a Farm that contains one or more RDS servers.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**farm**| [FarmId](vdi.entity.FarmId.md)|  Farm needed to create RDS Desktop. This Farm must not already be associated with another RDS desktop. [^2]
**cloudBrokered**|  xsd:boolean|  Indicates whether the RDS Desktop pool is brokered by cloud broker.  **_Since_** Horizon 8.2 [^5] [^1]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.