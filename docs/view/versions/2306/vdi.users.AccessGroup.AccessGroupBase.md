---
layout: page
title: Data Object - AccessGroupBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.AccessGroup.AccessGroupBase
Property of
     [AccessGroupInfo](vdi.users.AccessGroup.AccessGroupInfo.md#field_detail)
Parameter to
     [AccessGroup_Create](vdi.users.AccessGroup.md#create)
See also
     [AccessGroupId](vdi.entity.AccessGroupId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Base data used for access group creation. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The access group name.   


[^2]
  * This property must contain only alphanumerics, spaces, underscores, and dashes. The maximum length is 32 characters. 

  
**description**|  xsd:string|  The access group description.   


[^1]
[^2]
  * This property has a maximum length of 400 characters. 

  
**parent**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The AccessGroupId of the access group's parent. This is unset if this is the root access group.   


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

