---
layout: page
title: Data Object - DesktopBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.DesktopBase
Property of
     [DesktopInfo](vdi.resources.Desktop.DesktopInfo.md#field_detail), [DesktopProvisioningView](vdi.resources.Desktop.DesktopProvisioningView.md#field_detail), [DesktopSpec](vdi.resources.Desktop.DesktopSpec.md#field_detail)
See also
     [AccessGroupId](vdi.entity.AccessGroupId.md)
Since 
    Horizon View 6.0

## Data Object Description 

DesktopBase is a set of attributes used to uniquely identify and organize the desktop. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The desktop name is the unique name used to identify this desktop.   


[^2]
  * This property must contain only alphanumerics, underscores, and dashes. The maximum length is 64 characters. 

  
**displayName**|  xsd:string|  The display name is the name that users will see when they connect to view client. If the display name is left blank, the identifier will be used.   


[^1]
  * This property has a maximum length of 256 characters. 

  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  View access groups can organize the desktops in your organization. They can also be used for delegated administration. For RDS Desktop, this has to be same as that of the corresponding Farm.   
  
**description**|  xsd:string|  The description is a set of notes about the desktop.   


[^1]
  * This property has a maximum length of 1024 characters. 

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

