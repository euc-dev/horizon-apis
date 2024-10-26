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
**enableUIUsernameCaching**|  xsd:boolean|  For UI based clients: [^282] [^283]
Non UI based clients should ignore this property. [^6] [^1]
 


 


[^1]: This property need not be set.
[^6]: This property has a default value of true.
[^282]: If set true, UI clients should show a "Remember me" check box option on the login page.
[^283]: If set false, UI clients should not show the "Remember me" check box option on the login page.