---
layout: page
title: Data Object - GlobalURLRedirectionSchemeHandler
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.URLRedirection.GlobalURLSchemeAndHandler`

Property of
> [URLRedirectionData](vdi.infrastructure.URLRedirection.URLRedirectionData.md#field_detail)

See also
> [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)

Since
> Horizon 7.0.2


## Data Object Description

Data object having 1 on 1 mapping of URL Scheme/protocol with Global Resources (GlobalEntitlmentId or GlobalApplicationEntitlementId).

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**urlScheme**|  xsd:string|  URL Scheme/protocol used by View Client for URL Filtering.
**type**|  xsd:string| [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"APPLICATION"</td><td>Application Pool.</td></tr><tr><td>"DESKTOP"</td><td>Desktop Pool.</td></tr></table>
**gaeSchemeHandler**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  Global Application Entitlement that can handle this URL Scheme. [^1] [^203]
**geSchemeHandler**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Global Entitlement that should be used to launch URLs with this Scheme. [^1] [^204]


 
