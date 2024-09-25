---
layout: page
title: Data Object - UserHomeSiteResolutionData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.federation.UserHomeSite.UserHomeSiteResolutionData
Property of
     [UserHomeSiteResolutionInfo](vdi.federation.UserHomeSite.UserHomeSiteResolutionInfo.md#field_detail)
See also
     [SiteId](vdi.entity.SiteId.md), [UserHomeSiteId](vdi.entity.UserHomeSiteId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)
Since 
    Horizon 7.8

## Data Object Description 

User home site resolution for the GlobalEntitlement. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [UserHomeSiteId](vdi.entity.UserHomeSiteId.md)|  Id of the user home site configuration   


[^2]

  
**group**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The group via which the user gets this site as the home site.   


[^1]
[^2]

  
**groupName**|  xsd:string|  Name of the group via which the user gets this site as the home site.   


[^1]
[^2]

  
**site**| [SiteId](vdi.entity.SiteId.md)|  Home Site Id   


[^2]

  
**siteName**|  xsd:string|  Name of the home site.   


[^2]

  
**type**|  xsd:string|  Indicates whether the home site is assigned to the user or a group and is associate with the global entitlement or not   


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"DIRECT_USER"| If the home site override is associated with the global entitlement for the user.  
"DIRECT_GROUP"| If the home site override is associated with the global entitlement for the group.  
"DEFAULT_USER"| If the home site is assigned to the user.  
"DEFAULT_GROUP"| If the home site is assigned to the group.  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

