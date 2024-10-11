---
layout: page
title: Data Object - PermissionBase
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.Permission.PermissionBase`

Property of  
> [PermissionInfo](vdi.users.Permission.PermissionInfo.md#field_detail)

Parameter to  
> [Permission_Create](vdi.users.Permission.md#create), [Permission_CreatePermissions](vdi.users.Permission.md#createPermissions)

See also  
> [AccessGroupId](vdi.entity.AccessGroupId.md), [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md), [RoleId](vdi.entity.RoleId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since  
> Horizon View 6.0


## Data Object Description 

Base data used for permission creation. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user or group for this permission.   


* This property cannot be updated.

  
**role**| [RoleId](vdi.entity.RoleId.md)|  The role for this permission.   


* This property cannot be updated.

  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The access group for this permission. If the role is not applicable to access groups, specify the root access group.   


* This property need not be set.
* This property cannot be updated.

  
**globalAccessGroup**| [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)|  The global access group for this permission. If the role is applicable to global access groups, then it is required.  **_Since_** Horizon 8.2  


* This property need not be set.
* This property cannot be updated.

  
  
  

  
  
