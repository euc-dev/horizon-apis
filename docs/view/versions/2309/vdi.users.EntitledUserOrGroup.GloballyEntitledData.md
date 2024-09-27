---
layout: page
title: Data Object - EntitledUserOrGroupGloballyEntitledData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.EntitledUserOrGroup.GloballyEntitledData  
Property of
     [EntitledUserOrGroupGlobalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#field_detail), [EntitledUserOrGroupInfo](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo.md#field_detail)  
See also
     [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [PodAssignmentId](vdi.entity.PodAssignmentId.md), [URLRedirectionId](vdi.entity.URLRedirectionId.md), [UserEntitlementId](vdi.entity.UserEntitlementId.md), [UserHomeSiteId](vdi.entity.UserHomeSiteId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Data relevant to globally entitled users. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**globalEntitlements**| [GlobalEntitlementId[]](vdi.entity.GlobalEntitlementId.md)|  Global desktop entitlements for this user.   


 * This property need not be set.
  * This property is an unordered array of unique values.

  
**globalUserEntitlements**| [UserEntitlementId[]](vdi.entity.UserEntitlementId.md)|  Global entitlement user entitlements for this user or group. The array index will correspond to the same global entitlement as the GlobalEntitlementId array.   


 * This property need not be set.

  
**globalApplicationEntitlements**| [GlobalApplicationEntitlementId[]](vdi.entity.GlobalApplicationEntitlementId.md)|  Global application entitlements for this user.  **_Since_** Horizon View 6.2  


 * This property need not be set.
  * This property is an unordered array of unique values.

  
**globalUserApplicationEntitlements**| [UserEntitlementId[]](vdi.entity.UserEntitlementId.md)|  Global application entitlement user entitlements for this user or group. The array index will correspond to the same global application entitlement as the GlobalApplicationEntitlementId array.  **_Since_** Horizon View 6.2  


 * This property need not be set.

  
**userHomeSites**| [UserHomeSiteId[]](vdi.entity.UserHomeSiteId.md)|  Home sites for this user or group. There may be home site overrides for each global entitlement specified for this user or group and one default site for the user or group in general.   


 * This property need not be set.

  
**podAssignments**| [PodAssignmentId[]](vdi.entity.PodAssignmentId.md)|  Pod assignments per global entitlement, if any, for this user or group. If this is a group, this will be null.   


 * This property need not be set.

  
**urlRedirectionSettings**| [URLRedirectionId[]](vdi.entity.URLRedirectionId.md)|  Global URL Redirection settings associated with user or group.  **_Since_** Horizon 7.0.2  


 * This property need not be set.
  * This property is an unordered array of unique values.

  
**urlRedirectionUserEntitlements**| [UserEntitlementId[]](vdi.entity.UserEntitlementId.md)|  Global URLRedirection user entitlements for this user or group. The array index will correspond to the same urlRedirection entitlement as the URLRedirectionId array.  **_Since_** Horizon 7.0.2  


 * This property need not be set.
  * This property is an unordered array of unique values.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

