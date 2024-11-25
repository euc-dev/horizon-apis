---
layout: page
title: Data Object - DesktopAssignmentView
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.DesktopAssignmentView`

See also
> [DesktopAssignmentData](vdi.resources.Desktop.DesktopAssignmentData.md), [DesktopId](vdi.entity.DesktopId.md)

Since
> Horizon 7.9


## Data Object Description

Desktop id + Desktop assignment data which will include desktop pool information, operation system, global entitlement.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

The DesktopAssignmentView query service.

Query **Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  This query will return results only for desktops the caller has desktop read privilege on with the corresponding access group permission.
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read the [desktopAssignmentData](vdi.resources.Desktop.DesktopAssignmentView.md#desktopAssignmentData).[globalEntitlement](vdi.resources.Desktop.DesktopAssignmentData.md#globalEntitlement) member of a desktop. This will otherwise be unset.



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [DesktopId](vdi.entity.DesktopId.md)|  The id of the desktop.
**desktopAssignmentData**| [DesktopAssignmentData](vdi.resources.Desktop.DesktopAssignmentData.md)|  Core attributes of the desktop assignment instance.
**refId**|  xsd:string|  Reference ID used for this desktop pool.  **_Since_** Horizon 8.1 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.