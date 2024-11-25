---
layout: page
title: Data Object - URLRedirectionData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.URLRedirection.URLRedirectionData`

Property of
> [URLRedirectionInfo](vdi.infrastructure.URLRedirection.URLRedirectionInfo.md#field_detail), [URLRedirectionSpec](vdi.infrastructure.URLRedirection.URLRedirectionSpec.md#field_detail)

See also
> [GlobalURLRedirectionSchemeHandler](vdi.infrastructure.URLRedirection.GlobalURLSchemeAndHandler.md), [URLRedirectionSchemeHandler](vdi.infrastructure.URLRedirection.URLSchemeAndHandler.md)

Since
> Horizon 7.0


## Data Object Description

URL Redirection Data Object.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**displayName**|  xsd:string|  The URLRedirection name is the display name for this Setting. [^12]
**description**|  xsd:string|  The description is set of notes about the URLRedirection Setting. [^1] [^13]
**enabled**|  xsd:boolean|  Whether or not this URLRedirection Setting is enabled or not. [^6]
**scope**|  xsd:string|  Represent whether this URL Redirection setting is local (LOCAL) or global (GLOBAL) level.  **_Since_** Horizon 7.0.2 [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"LOCAL"</td><td>Local URL Redirection Setting.</td></tr><tr><td>"GLOBAL"</td><td>Global URL Redirection Setting.</td></tr></table>
**urlSchemeAndHandlers**| [URLRedirectionSchemeHandler[]](vdi.infrastructure.URLRedirection.URLSchemeAndHandler.md)|  URL Scheme and Local resource (Desktop or Application Pool) mappings. [^1] [^14]
**globalURLSchemeAndHandlers**| [GlobalURLRedirectionSchemeHandler[]](vdi.infrastructure.URLRedirection.GlobalURLSchemeAndHandler.md)|  URL Scheme and Global resource (GE or GAE) mappings.  **_Since_** Horizon 7.0.2 [^1] [^14]
**urlAgentPatterns**|  xsd:string[]|  List of URL patterns/Regular expression that must be opened on Agent machine. [^1] [^14]
**urlClientPatterns**|  xsd:string[]|  List of URL patterns/Regular expression that must be opened on client machine. [^1] [^14]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^6]: This property has a default value of true.
[^12]: This property has a maximum length of 256 characters.
[^13]: This property has a maximum length of 1024 characters.
[^14]: This property is an unordered array of unique values.