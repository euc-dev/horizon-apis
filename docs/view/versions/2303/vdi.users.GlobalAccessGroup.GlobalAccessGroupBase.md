---
layout: page
title: Data Object - GlobalAccessGroupBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.GlobalAccessGroup.GlobalAccessGroupBase  
Property of
     [GlobalAccessGroupInfo](vdi.users.GlobalAccessGroup.GlobalAccessGroupInfo.md#field_detail)  
Parameter to
     [GlobalAccessGroup_Create](vdi.users.GlobalAccessGroup.md#create)  
See also
     [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)  
Since 
    Horizon 8.2

## Data Object Description 

Base data used for global access group creation. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The global access group name.   


* This property cannot be updated.
  * This property must contain only alphanumerics, spaces, underscores, and dashes. The maximum length is 32 characters. 

  
**description**|  xsd:string|  The global access group description.   


* This property need not be set.
* This property cannot be updated.
  * This property has a maximum length of 400 characters. 

  
**parent**| [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)|  The GlobalAccessGroupId of the access group's parent. This is unset if this is the root access group.   


* This property need not be set.
* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

