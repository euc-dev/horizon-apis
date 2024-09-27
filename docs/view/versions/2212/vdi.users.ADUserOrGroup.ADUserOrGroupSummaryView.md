---
layout: page
title: Data Object - ADUserOrGroupSummaryView
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView  
Property of
     [ADUserOrGroupView](vdi.users.ADUserOrGroup.ADUserOrGroupView.md#field_detail)  
Returned by
     [ADUserOrGroup_GetSummaryView](vdi.users.ADUserOrGroup.md#getSummaryView), [ADUserOrGroup_GetSummaryViews](vdi.users.ADUserOrGroup.md#getSummaryViews), [ADUserOrGroup_Refresh](vdi.users.ADUserOrGroup.md#refresh), [ADUserOrGroup_RefreshUsersOrGroups](vdi.users.ADUserOrGroup.md#refreshUsersOrGroups)  
See also
     [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Summary view for ADUserOrGroup. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

Query definitions can specify the following member types: 

  * [base](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md#base).[group](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#group) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [base](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md#base).[loginName](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#loginName)/[name](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#name) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only) 
  * [base](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md#base).[domain](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#domain) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only). This can be specified as either the DNS or NetBIOS name of the domain. 
  * [base](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md#base).[description](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#description) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only) 
  * [base](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md#base).[phone](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#phone) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only) 
  * [base](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md#base).[email](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#email) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only) 
  * [base](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md#base).[guid](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#guid) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [base](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md#base).[formattedGuid](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#formattedGuid) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 

The following caveats apply: 
  * The first filter may be any of the above or an [QueryFilterAnd](vdi.query.QueryFilter.And.md) filter specifying any combination of the above. An Or filter is also allowed, but only in two valid scenarios: 
    * it specifies (group=true AND group=false). This signifies a query that should return both users and groups. 
    * it specifies multiple domain with [QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter. This signifies a query that should search users or groups in all the specified domains.  
**Note:** If more than one domain is passed then it will gracefully ignore any exceptions occurred during search in any of the domains. 
  * The default query searches both users and groups for any all usernames, names, domains, and descriptions.
  * If either name or username is specified in a filter, the query will be done on both of these fields regardless of which is specified. 
  * If [sortBy](vdi.query.QueryDefinition.md#sortBy) is specified, only the first [limit](vdi.query.QueryDefinition.md#limit) results in the system will be included.
  * [limit](vdi.query.QueryDefinition.md#limit) cannot exceed 2000.
  * [startingOffset](vdi.query.QueryDefinition.md#startingOffset) cannot be specified.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or group ID of this entity.   
  
**base**| [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md)|  Basic active directory data for a user or group.   
  
  
  
  
  
  

