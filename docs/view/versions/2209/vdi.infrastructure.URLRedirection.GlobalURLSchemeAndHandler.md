---
layout: page
title: Data Object - GlobalURLRedirectionSchemeHandler
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.URLRedirection.GlobalURLSchemeAndHandler  
Property of
     [URLRedirectionData](vdi.infrastructure.URLRedirection.URLRedirectionData.md#field_detail)  
See also
     [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)  
Since 
    Horizon 7.0.2

## Data Object Description 

Data object having 1 on 1 mapping of URL Scheme/protocol with Global Resources (GlobalEntitlmentId or GlobalApplicationEntitlementId). 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**urlScheme**|  xsd:string|  URL Scheme/protocol used by View Client for URL Filtering.   
  
**type**|  xsd:string|    


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"APPLICATION"| Application Pool.  
"DESKTOP"| Desktop Pool.  

  
**gaeSchemeHandler**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  Global Application Entitlement that can handle this URL Scheme.   


* This property need not be set.
  * This property is required if type is set to "APPLICATION".

  
**geSchemeHandler**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Global Entitlement that should be used to launch URLs with this Scheme.   


* This property need not be set.
  * This property is required if type is set to "DESKTOP".

  
  
  
 
  
  

