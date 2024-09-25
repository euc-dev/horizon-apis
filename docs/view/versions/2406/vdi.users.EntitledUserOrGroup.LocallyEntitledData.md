---
layout: page
title: Data Object - EntitledUserOrGroupLocallyEntitledData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.EntitledUserOrGroup.LocallyEntitledData
Property of
     [EntitledUserOrGroupInfo](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo.md#field_detail), [EntitledUserOrGroupLocalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#field_detail)
See also
     [ApplicationId](vdi.entity.ApplicationId.md), [DesktopId](vdi.entity.DesktopId.md), [MachineId](vdi.entity.MachineId.md), [PersistentDiskId](vdi.entity.PersistentDiskId.md), [URLRedirectionId](vdi.entity.URLRedirectionId.md), [UserEntitlementId](vdi.entity.UserEntitlementId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Data relevant to locally entitled users. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**machines**| [MachineId[]](vdi.entity.MachineId.md)|  Machines this user or group is assigned to. MachineIds of this type originate from the [Machine](vdi.resources.Machine.md) service.   


[^1]
  * This property is an unordered array of unique values.

  
**persistentDisks**| [PersistentDiskId[]](vdi.entity.PersistentDiskId.md)| **Deprecated.**_This property is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ View Composer persistent disks this user is assigned to.   


[^1]
  * This property is an unordered array of unique values.

  
**persistentDiskRefIds**|  xsd:string[]|  Reference IDs of the persistent disk(s) this user is assigned to.  **_Since_** Horizon 8.10  


[^1]
[^2]

  
**desktops**| [DesktopId[]](vdi.entity.DesktopId.md)|  Local desktops for which this user has an entitlement.   


[^1]
  * This property is an unordered array of unique values.

  
**desktopUserEntitlements**| [UserEntitlementId[]](vdi.entity.UserEntitlementId.md)|  Local desktop user entitlements for this user or group. The array index will correspond to the same desktop entitlement as the DesktopId array.   


[^1]

  
**applications**| [ApplicationId[]](vdi.entity.ApplicationId.md)|  Local applications for which this user has an entitlement.   


[^1]
  * This property is an unordered array of unique values.

  
**applicationUserEntitlements**| [UserEntitlementId[]](vdi.entity.UserEntitlementId.md)|  Local application user entitlements for this user or group. The array index will correspond to the same application entitlement as the ApplicationId array.   


[^1]

  
**urlRedirectionSettings**| [URLRedirectionId[]](vdi.entity.URLRedirectionId.md)|  Local URL Redirection settings associated with user or group.  **_Since_** Horizon 7.0  


[^1]
  * This property is an unordered array of unique values.

  
**urlRedirectionUserEntitlements**| [UserEntitlementId[]](vdi.entity.UserEntitlementId.md)|  URLRedirection user entitlements for this user or group. The array index will correspond to the same urlRedirection entitlement as the URLRedirectionId array.  **_Since_** Horizon 7.0  


[^1]
  * This property is an unordered array of unique values.

  
  

  

