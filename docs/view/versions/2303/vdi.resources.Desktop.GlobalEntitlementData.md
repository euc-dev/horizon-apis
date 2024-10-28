---
layout: page
title: Data Object - DesktopGlobalEntitlementData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.GlobalEntitlementData`

Property of
> [DesktopInfo](vdi.resources.Desktop.DesktopInfo.md#field_detail), [DesktopSpec](vdi.resources.Desktop.DesktopSpec.md#field_detail)

See also
> [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)

Since
> Horizon View 6.0


## Data Object Description

Data for Global Entitlement.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Global entitlement for this desktop. This member will be null if not set or caller does not have global read permissions. [^1]
**globalEntitlementName**|  xsd:string|  Name of global entitlement for this desktop pool. This member will be populated even if caller does not have global read permissions.  **_Since_** Horizon 8.2 [^1]
 


 


[^1]: This property need not be set.