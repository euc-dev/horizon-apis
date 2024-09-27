---
layout: page
title: Data Object - ADUserOrGroupView
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.ADUserOrGroup.ADUserOrGroupView  
Returned by
     [ADUserOrGroup_GetView](vdi.users.ADUserOrGroup.md#getView), [ADUserOrGroup_GetViews](vdi.users.ADUserOrGroup.md#getViews)  
See also
     [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md), [ADUserOrGroupExtendedData](vdi.users.ADUserOrGroup.ADUserOrGroupExtendedData.md), [ADUserOrGroupSummaryView](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Full View for ADUserOrGroup 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or group ID of this entity.   
  
**base**| [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md)|  Basic active directory data for a user or group.   
  
**extendedData**| [ADUserOrGroupExtendedData](vdi.users.ADUserOrGroup.ADUserOrGroupExtendedData.md)|  Computed data about this user or group.   
  
**groupSVs**| [ADUserOrGroupSummaryView[]](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md)|  Summary views of the group it belongs to.   


 * This property need not be set.

  
  
  
   
  
  

