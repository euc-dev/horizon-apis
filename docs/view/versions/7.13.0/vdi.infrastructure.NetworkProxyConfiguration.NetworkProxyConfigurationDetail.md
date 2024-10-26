---
layout: page
title: Data Object - NetworkProxyConfigurationDetail
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.NetworkProxyConfiguration.NetworkProxyConfigurationDetail`

Returned by
> [NetworkProxyConfiguration_Get](vdi.infrastructure.NetworkProxyConfiguration.md#get)

See also
> [SecureString](vdi.util.SecureString.md)

Since
> Horizon 7.3


## Data Object Description

Network proxy configuration details.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**networkAutoProxy**|  xsd:boolean|  Whether auto-proxy is enabled.
**networkProxyHostname**|  xsd:string|  Network proxy host name. [^1] [^293]
**networkProxyPort**|  xsd:int|  Network proxy port. [^1] [^8] [^189] [^293]
**networkProxyUsername**|  xsd:string|  Network proxy user name. [^1]
**networkProxyPassword**| [SecureString](vdi.util.SecureString.md)|  Network proxy password. [^1]


 
