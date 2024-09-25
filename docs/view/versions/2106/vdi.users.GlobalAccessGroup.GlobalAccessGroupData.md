---
layout: page
title: Data Object - GlobalAccessGroupData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.GlobalAccessGroup.GlobalAccessGroupData
Property of
     [GlobalAccessGroupInfo](vdi.users.GlobalAccessGroup.GlobalAccessGroupInfo.md#field_detail)
See also
     [PermissionId](vdi.entity.PermissionId.md)
Since 
    Horizon 8.2

## Data Object Description 

Readonly data about this global access group. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**permissions**| [PermissionId[]](vdi.entity.PermissionId.md)|  Administrative permissions (user/group and role) for this global access group.   


[^1]

  
**isDeletable**|  xsd:boolean|  If true, the global access group can be deleted, else not. For root global access group, the value will always be false.   


  * This property has a default value of false.
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
