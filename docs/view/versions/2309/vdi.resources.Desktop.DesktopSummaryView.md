---
layout: page
title: Data Object - DesktopSummaryView
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.DesktopSummaryView`

Returned by  
> [Desktop_GetSummaryView](vdi.resources.Desktop.md#getSummaryView), [Desktop_GetSummaryViews](vdi.resources.Desktop.md#getSummaryViews), [Desktop_ListGECompatibleDesktops](vdi.resources.Desktop.md#listGECompatibleDesktops)

See also  
> [DesktopId](vdi.entity.DesktopId.md), [DesktopSummaryData](vdi.resources.Desktop.DesktopSummaryData.md)

Since  
> Horizon View 6.0


## Data Object Description 

Desktop id + global entitlement id + summary data. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

The DesktopSummaryView query service example api to get all Users/groups entitled/associated to particular Global entitlement. 

Query Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  This query will return results only for desktops the caller has desktop read privilege on with the corresponding access group permission.   
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read the [desktopSummaryData](vdi.resources.Desktop.DesktopSummaryView.md#desktopSummaryData).[globalEntitlement](vdi.resources.Desktop.DesktopSummaryData.md#globalEntitlement) member of a desktop. This will otherwise be unset.   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [DesktopId](vdi.entity.DesktopId.md)|  The id of the desktop.   
  
**desktopSummaryData**| [DesktopSummaryData](vdi.resources.Desktop.DesktopSummaryData.md)|  Core attributes of the desktop instance.   
  
**refId**|  xsd:string|  Reference ID used for this desktop pool.  **_Since_** Horizon 8.1  


 * This property need not be set.
 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
