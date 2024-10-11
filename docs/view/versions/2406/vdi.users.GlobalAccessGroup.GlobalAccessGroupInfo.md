---
layout: page
title: Data Object - GlobalAccessGroupInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.GlobalAccessGroup.GlobalAccessGroupInfo`

Returned by  
> [GlobalAccessGroup_Get](vdi.users.GlobalAccessGroup.md#get), [GlobalAccessGroup_List](vdi.users.GlobalAccessGroup.md#list)

See also  
> [GlobalAccessGroupBase](vdi.users.GlobalAccessGroup.GlobalAccessGroupBase.md), [GlobalAccessGroupData](vdi.users.GlobalAccessGroup.GlobalAccessGroupData.md), [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)

Since  
> Horizon 8.2


## Data Object Description 

The full global access group information. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)|  Global Access group id of this entity.   


 * This property cannot be updated.

  
**base**| [GlobalAccessGroupBase](vdi.users.GlobalAccessGroup.GlobalAccessGroupBase.md)|  Base data used for global access group creation.   


 * This property cannot be updated.

  
**data**| [GlobalAccessGroupData](vdi.users.GlobalAccessGroup.GlobalAccessGroupData.md)|  Readonly data about this global access group.   


 * This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this global access group.  **_Since_** Horizon 8.3  


 * This property need not be set.
 * This property cannot be updated.

  
  

  
