---
layout: page
title: Data Object - AccessGroupInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.AccessGroup.AccessGroupInfo`

Property of  
> [AccessGroupInfo](vdi.users.AccessGroup.AccessGroupInfo.md#field_detail), [AdminUserOrGroupView](vdi.users.AdminUserOrGroup.AdminUserOrGroupView.md#field_detail)

Returned by  
> [AccessGroup_Get](vdi.users.AccessGroup.md#get), [AccessGroup_List](vdi.users.AccessGroup.md#list)

See also  
> [AccessGroupBase](vdi.users.AccessGroup.AccessGroupBase.md), [AccessGroupData](vdi.users.AccessGroup.AccessGroupData.md), [AccessGroupId](vdi.entity.AccessGroupId.md),

Since  
> Horizon View 6.0


## Data Object Description 

The full access group information. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  Access group id of this entity.   


* This property cannot be updated.

  
**base**| [AccessGroupBase](vdi.users.AccessGroup.AccessGroupBase.md)|  Base data used for access group creation.   


* This property cannot be updated.

  
**data**| [AccessGroupData](vdi.users.AccessGroup.AccessGroupData.md)|  Readonly data about this access group.   


* This property cannot be updated.

  
**children**| [AccessGroupInfo[]](vdi.users.AccessGroup.AccessGroupInfo.md)|  An array of AccessGroupInfo for this access group children.   


* This property need not be set.
* This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID for this access group.  **_Since_** Horizon 8.2  


* This property need not be set.
* This property cannot be updated.

  
  
  
 
  
  
