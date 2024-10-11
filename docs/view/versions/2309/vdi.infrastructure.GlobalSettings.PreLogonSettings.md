---
layout: page
title: Data Object - GlobalPreLogonSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.PreLogonSettings`

Returned by  
> [GlobalSettings_GetPreLogonSettings](vdi.infrastructure.GlobalSettings.md#getPreLogonSettings)

Since  
> Horizon 7.5


## Data Object Description 

The Configuration which can be accessed without any user authentication on the login page. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**enableUIUsernameCaching**|  xsd:boolean|  For UI based clients: 

  * if set true, UI clients should show a "Remember me" check box option on login page.
  * if set false, UI clients should not show the "Remember me" check box option on login page.

Non UI based clients should ignore this property.   


  * This property has a default value of true.
 * This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
