---
layout: page
title: Data Object - AdminUserOrGroupPrivilegesInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.AdminUserOrGroup.AdminUserOrGroupPrivilegesInfo  
Property of
     [AdminUserOrGroupLoginView](vdi.users.AdminUserOrGroup.AdminUserOrGroupLoginView.md#field_detail)  
See also
     [AccessGroupId](vdi.entity.AccessGroupId.md), [AccessGroupSummaryView](vdi.users.AccessGroup.AccessGroupSummaryView.md)  
Since 
    Horizon 7.5

## Data Object Description 

Represents access group and privileges mapping for the user or group. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**accessGroupId**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The access group id.   
  
**accessGroupName**|  xsd:string|  The access group name.   
  
**privileges**|  xsd:string[]|  The set of privileges on the current access group.   
  
**children**| [AccessGroupSummaryView[]](vdi.users.AccessGroup.AccessGroupSummaryView.md)|  Child access groups associated with current access group.  **_Since_** Horizon 7.6  


* This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

