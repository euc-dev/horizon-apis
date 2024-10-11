---
layout: page
title: Data Object - AccessGroupBase
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.AccessGroup.AccessGroupBase`

Property of  
> [AccessGroupInfo](vdi.users.AccessGroup.AccessGroupInfo.md#field_detail)

Parameter to  
> [AccessGroup_Create](vdi.users.AccessGroup.md#create)

See also  
> [AccessGroupId](vdi.entity.AccessGroupId.md)

Since  
> Horizon View 6.0


## Data Object Description 

Base data used for access group creation. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The access group name.   


 * This property cannot be updated.
  * This property must contain only alphanumerics, spaces, underscores, and dashes. The maximum length is 32 characters. 

  
**description**|  xsd:string|  The access group description.   


 * This property need not be set.
 * This property cannot be updated.
  * This property has a maximum length of 400 characters. 

  
**parent**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The AccessGroupId of the access group's parent. This is unset if this is the root access group.   


 * This property need not be set.
 * This property cannot be updated.

  
  

  
