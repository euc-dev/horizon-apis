---
layout: page
title: Data Object - UserHomeSitesSpec
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.federation.UserHomeSite.UserHomeSitesSpec`

Parameter to
> [UserHomeSite_CreateOrUpdate](vdi.federation.UserHomeSite.md#createOrUpdate)

See also
> [UserHomeSiteBase](vdi.federation.UserHomeSite.UserHomeSiteBase.md)

Since
> Horizon 7.9


## Data Object Description

User home site specification.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**allowUpdate**|  xsd:boolean|  determines whether the api can override an existing homesite. [^1]
**bases**| [UserHomeSiteBase[]](vdi.federation.UserHomeSite.UserHomeSiteBase.md)|  List of Base data for user home site configuration.
 


 


[^1]: This property need not be set.