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
  
**type**|  xsd:string|  **_Since_** Horizon 7.0.2  


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"APPLICATION"| Application Pool.  
"DESKTOP"| Desktop Pool.  

  
**urlSchemeHandler**| [ApplicationId](vdi.entity.ApplicationId.md)|  Application that can handle this URL Scheme.  **_Since_** Horizon 7.0.2  


 * This property need not be set.
  * This property is required if type is set to "APPLICATION".

  
**desktopSchemeHandler**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop Pool that should be used to launch URLs with this Scheme.  **_Since_** Horizon 7.0.2  


 * This property need not be set.
  * This property is required if type is set to "DESKTOP".

  
  

  
