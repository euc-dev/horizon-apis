---
layout: page
title: Data Object - GlobalAdminUserOrGroupPrivilegesInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.AdminUserOrGroup.GlobalAdminUserOrGroupPrivilegesInfo
Property of
     [AdminUserOrGroupLoginView](vdi.users.AdminUserOrGroup.AdminUserOrGroupLoginView.md#field_detail)
See also
     [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md), [GlobalAccessGroupSummaryView](vdi.users.GlobalAccessGroup.GlobalAccessGroupSummaryView.md)
Since 
    Horizon 8.2

## Data Object Description 

Represents global access group and privileges mapping for the user or group. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**globalAccessGroupId**| [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)|  The global access group id.   


[^1]

  
**globalAccessGroupName**|  xsd:string|  The global access group name.   
  
**privileges**|  xsd:string[]|  The set of privileges on the current global access group.   


[^1]

  
**children**| [GlobalAccessGroupSummaryView[]](vdi.users.GlobalAccessGroup.GlobalAccessGroupSummaryView.md)|  Child access groups associated with current global access group.   


[^1]

  
  

  

