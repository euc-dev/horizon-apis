---
layout: page
title: Data Object - NetworkProxyConfigurationDetail
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.NetworkProxyConfiguration.NetworkProxyConfigurationDetail`

Returned by
> [NetworkProxyConfiguration_Get](vdi.infrastructure.NetworkProxyConfiguration.md#get)

See also
> [SecureString](vdi.util.SecureString.md)

Since
> Horizon 7.3


## Data Object Description

Network proxy configuration details.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**networkAutoProxy**|  xsd:boolean|  Whether auto-proxy is enabled.
**networkProxyHostname**|  xsd:string|  Network proxy host name. [^1] [^293]
**networkProxyPort**|  xsd:int|  Network proxy port. [^1] [^8] [^189] [^293]
**networkProxyUsername**|  xsd:string|  Network proxy user name. [^1]
**networkProxyPassword**| [SecureString](vdi.util.SecureString.md)|  Network proxy password. [^1]


 


[^1]: This property need not be set.
[^8]: This property has a minimum value of 1.
[^189]: This property has a maximum value of 65535.
[^293]: This property is required if networkAutoProxy is set to false.