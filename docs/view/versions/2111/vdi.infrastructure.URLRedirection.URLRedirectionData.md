---
layout: page
title: Data Object - URLRedirectionData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.URLRedirection.URLRedirectionData  
Property of
     [URLRedirectionInfo](vdi.infrastructure.URLRedirection.URLRedirectionInfo.md#field_detail), [URLRedirectionSpec](vdi.infrastructure.URLRedirection.URLRedirectionSpec.md#field_detail)  
See also
     [GlobalURLRedirectionSchemeHandler](vdi.infrastructure.URLRedirection.GlobalURLSchemeAndHandler.md), [URLRedirectionSchemeHandler](vdi.infrastructure.URLRedirection.URLSchemeAndHandler.md)  
Since 
    Horizon 7.0

## Data Object Description 

URL Redirection Data Object. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**displayName**|  xsd:string|  The URLRedirection name is the display name for this Setting.   


  * This property has a maximum length of 256 characters. 

  
**description**|  xsd:string|  The description is set of notes about the URLRedirection Setting.   


* This property need not be set.
  * This property has a maximum length of 1024 characters. 

  
**enabled**|  xsd:boolean|  Whether or not this URLRedirection Setting is enabled or not.   


  * This property has a default value of true.

  
**scope**|  xsd:string|  Represent whether this URL Redirection setting is local (LOCAL) or global (GLOBAL) level.  **_Since_** Horizon 7.0.2  


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"LOCAL"| Local URL Redirection Setting.  
"GLOBAL"| Global URL Redirection Setting.  

  
**urlSchemeAndHandlers**| [URLRedirectionSchemeHandler[]](vdi.infrastructure.URLRedirection.URLSchemeAndHandler.md)|  URL Scheme and Local resource (Desktop or Application Pool) mappings.   


* This property need not be set.
  * This property is an unordered array of unique values.

  
**globalURLSchemeAndHandlers**| [GlobalURLRedirectionSchemeHandler[]](vdi.infrastructure.URLRedirection.GlobalURLSchemeAndHandler.md)|  URL Scheme and Global resource (GE or GAE) mappings.  **_Since_** Horizon 7.0.2  


* This property need not be set.
  * This property is an unordered array of unique values.

  
**urlAgentPatterns**|  xsd:string[]|  List of URL patterns/Regular expression that must be opened on Agent machine.   


* This property need not be set.
  * This property is an unordered array of unique values.

  
**urlClientPatterns**|  xsd:string[]|  List of URL patterns/Regular expression that must be opened on client machine.   


* This property need not be set.
  * This property is an unordered array of unique values.

  
  
  
   
  
  

