---
layout: page
title: Data Object - PermissionNamesData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.Permission.PermissionNamesData`

Property of
> [PermissionInfo](vdi.users.Permission.PermissionInfo.md#field_detail)

Since
> Horizon 7.8


## Data Object Description

Names data of User, Role and AccessGroup involved in the permission.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**userOrGroupName**|  xsd:string|  Name of the user or group for this permission. [^2]
**roleName**|  xsd:string|  Name of the role for this permission. [^2]
**accessGroupName**|  xsd:string|  Name of the access group for this permission. [^2]


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.