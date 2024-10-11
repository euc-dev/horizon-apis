---
layout: page
title: Data Object - AccessGroupData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.AccessGroup.AccessGroupData`

Property of  
> [AccessGroupInfo](vdi.users.AccessGroup.AccessGroupInfo.md#field_detail)

See also  
> [PermissionId](vdi.entity.PermissionId.md)

Since  
> Horizon View 6.0


## Data Object Description 

Readonly data about this access group. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**permissions**| [PermissionId[]](vdi.entity.PermissionId.md)|  Administrative permissions (user/group and role) for this access group.   


 * This property need not be set.

  
**isDeletable**|  xsd:boolean|  If true, the access group can be deleted, else not. For root access group, the value will always be false.  **_Since_** Horizon 7.8  


  * This property has a default value of false.
 * This property cannot be updated.

  
  

  
