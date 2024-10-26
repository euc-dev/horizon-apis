---
layout: page
title: Data Object - URLRedirectionSchemeHandler
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.URLRedirection.URLSchemeAndHandler`

Property of
> [URLRedirectionData](vdi.infrastructure.URLRedirection.URLRedirectionData.md#field_detail)

See also
> [ApplicationId](vdi.entity.ApplicationId.md), [DesktopId](vdi.entity.DesktopId.md)

Since
> Horizon 7.0


## Data Object Description

Data object having 1 on 1 mapping of URL Scheme/protocol with Local Resources (DesktopId or ApplicationId).

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**urlScheme**|  xsd:string|  URL Scheme/protocol used by View Client for URL Filtering.
**type**|  xsd:string|  **_Since_** Horizon 7.0.2 [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"APPLICATION"</td><td>Application Pool.</td></tr><tr><td>"DESKTOP"</td><td>Desktop Pool.</td></tr></table>
**urlSchemeHandler**| [ApplicationId](vdi.entity.ApplicationId.md)|  Application that can handle this URL Scheme.  **_Since_** Horizon 7.0.2 [^1] [^203]
**desktopSchemeHandler**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop Pool that should be used to launch URLs with this Scheme.  **_Since_** Horizon 7.0.2 [^1] [^204]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^203]: This property is required if type is set to "APPLICATION".
[^204]: This property is required if type is set to "DESKTOP".