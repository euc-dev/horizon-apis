---
layout: page
title: Data Object - JwtTokenInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.JwtToken.JwtTokenInfo`

Returned by
> [JwtToken_Generate](vdi.infrastructure.JwtToken.md#generate)

Since
> Horizon 7.4


## Data Object Description

JWT token info.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**token**|  xsd:string|  JWT token.
**expiryTime**|  xsd:dateTime|  Token expiry time. [^1]
 


 


[^1]: This property need not be set.