---
layout: page
title: Data Object - AccessGroupData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.AccessGroup.AccessGroupData
Property of
     [AccessGroupInfo](vdi.users.AccessGroup.AccessGroupInfo.md#field_detail)
See also
     [PermissionId](vdi.entity.PermissionId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Readonly data about this access group. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**permissions**| [PermissionId[]](vdi.entity.PermissionId.md)|  Administrative permissions (user/group and role) for this access group.   


[^1]

  
**isDeletable**|  xsd:boolean|  If true, the access group can be deleted, else not. For root access group, the value will always be false.  **_Since_** Horizon 7.8  


  * This property has a default value of false.
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
