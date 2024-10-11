---
layout: page
title: Data Object - AdminUserOrGroupView
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.AdminUserOrGroup.AdminUserOrGroupView`

Property of  
> [AdminUserOrGroupView](vdi.users.AdminUserOrGroup.AdminUserOrGroupView.md#field_detail)

Returned by  
> [AdminUserOrGroup_GetView](vdi.users.AdminUserOrGroup.md#getView), [AdminUserOrGroup_ListViews](vdi.users.AdminUserOrGroup.md#listViews)

See also  
> [AccessGroupInfo](vdi.users.AccessGroup.AccessGroupInfo.md), [AdminUserOrGroupInfo](vdi.users.AdminUserOrGroup.AdminUserOrGroupInfo.md), [PermissionInfo](vdi.users.Permission.PermissionInfo.md), [RoleInfo](vdi.users.Role.RoleInfo.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since  
> Horizon View 6.0


## Data Object Description 

Full view for AdminUserOrGroup. Contains recursive group membership information. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or group ID of this entity.   
  
**info**| [AdminUserOrGroupInfo](vdi.users.AdminUserOrGroup.AdminUserOrGroupInfo.md)|  Info for this AdminUserOrGroup.   
  
**permissions**| [PermissionInfo[]](vdi.users.Permission.PermissionInfo.md)|  Administrative permissions (roles and access groups) for this user or group.   


* This property need not be set.

  
**roles**| [RoleInfo[]](vdi.users.Role.RoleInfo.md)|  Set of roles this user or group has any permissions for. Cross reference with permissions member to determine the actual associated permission.   


* This property need not be set.

  
**accessGroups**| [AccessGroupInfo[]](vdi.users.AccessGroup.AccessGroupInfo.md)|  Set of access groups this user or group has any permission for. Cross reference with permissions member to determine the actual associated permission.   


* This property need not be set.

  
**groupViews**| [AdminUserOrGroupView[]](vdi.users.AdminUserOrGroup.AdminUserOrGroupView.md)|  Full views of this user or group's groups.   


* This property need not be set.

  
  
  
  
  
  
