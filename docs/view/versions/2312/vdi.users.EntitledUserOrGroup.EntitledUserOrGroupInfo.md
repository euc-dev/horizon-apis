---
layout: page
title: Data Object - EntitledUserOrGroupInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo  
Returned by
     [EntitledUserOrGroup_Get](vdi.users.EntitledUserOrGroup.md#get), [EntitledUserOrGroup_GetInfos](vdi.users.EntitledUserOrGroup.md#getInfos)  
See also
     [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md), [EntitledUserOrGroupGloballyEntitledData](vdi.users.EntitledUserOrGroup.GloballyEntitledData.md), [EntitledUserOrGroupLocallyEntitledData](vdi.users.EntitledUserOrGroup.LocallyEntitledData.md), [EntitledUserOrGroupUserSessionData](vdi.users.EntitledUserOrGroup.UserSessionData.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

The root entitled user or group information. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or group ID of this entity.   


 * This property cannot be updated.

  
**base**| [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md)|  Basic active directory data for a user or group.   


 * This property cannot be updated.

  
**localData**| [EntitledUserOrGroupLocallyEntitledData](vdi.users.EntitledUserOrGroup.LocallyEntitledData.md)|  Data relevant to locally entitled users. If no local data exists or is not permitted, this will contain only null members.   


 * This property need not be set.
 * This property cannot be updated.

  
**sessionData**| [EntitledUserOrGroupUserSessionData](vdi.users.EntitledUserOrGroup.UserSessionData.md)|  Data relevant to sessions for this user or group.   


 * This property need not be set.
 * This property cannot be updated.

  
**globalData**| [EntitledUserOrGroupGloballyEntitledData](vdi.users.EntitledUserOrGroup.GloballyEntitledData.md)|  Data relevant to globally entitled users. If Multi-Data Center View is not enabled, this is null. If no global data exists or is not permitted, this will contain only null members.   


 * This property need not be set.
 * This property cannot be updated.

  
  
  
   
  
  

