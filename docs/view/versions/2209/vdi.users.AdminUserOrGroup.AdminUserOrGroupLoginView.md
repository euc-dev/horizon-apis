---
layout: page
title: Data Object - AdminUserOrGroupLoginView
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.AdminUserOrGroup.AdminUserOrGroupLoginView`

Returned by  
> [AdminUserOrGroup_GetLoginView](vdi.users.AdminUserOrGroup.md#getLoginView), [AdminUserOrGroup_GetLoginViewById](vdi.users.AdminUserOrGroup.md#getLoginViewById)

See also  
> [AdminUserOrGroupPrivilegesInfo](vdi.users.AdminUserOrGroup.AdminUserOrGroupPrivilegesInfo.md), [GlobalAdminUserOrGroupPrivilegesInfo](vdi.users.AdminUserOrGroup.GlobalAdminUserOrGroupPrivilegesInfo.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since  
> Horizon 7.5


## Data Object Description 

Login view for AdminUserOrGroup. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or group ID of this entity.   
  
**privilegesInfo**| [AdminUserOrGroupPrivilegesInfo[]](vdi.users.AdminUserOrGroup.AdminUserOrGroupPrivilegesInfo.md)|  Set of privileges information based on Access Groups for this user or group.   
  
**globalPrivilegesInfo**| [GlobalAdminUserOrGroupPrivilegesInfo[]](vdi.users.AdminUserOrGroup.GlobalAdminUserOrGroupPrivilegesInfo.md)|  Set of privileges information based on Global Access Groups for this user or group.  **_Since_** Horizon 8.2  


* This property need not be set.

  
**helpdeskAdmin**|  xsd:boolean|  Indicates if the administrator is a Helpdesk administrator. This will be set to true if: 

  * Admin user has single role which is of type either HELP_DESK_ADMIN or HELP_DESK_ADMIN_READ_ONLY.

**_Since_** Horizon 7.11  


  * This property has a default value of false.

  
  
  
 
  
  
