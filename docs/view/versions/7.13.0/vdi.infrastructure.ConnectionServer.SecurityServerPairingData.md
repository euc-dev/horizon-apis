---
layout: page
title: Data Object - ConnectionServerSecurityServerPairingData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.SecurityServerPairingData`

Property of
> [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md#field_detail)

See also
> [SecureString](vdi.util.SecureString.md)

Since
> Horizon View 6.0


## Data Object Description

The Security Server pairing data.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**pairingPassword**| [SecureString](vdi.util.SecureString.md)|  The Security Server pairing password.
**timeoutMinutes**|  xsd:int|  The timeout of the pairing password (in minutes). [^8] [^253]


 


[^8]: This property has a minimum value of 1.
[^167]: This data object must be updated as a whole.
[^253]: This property has a maximum value of 1440.