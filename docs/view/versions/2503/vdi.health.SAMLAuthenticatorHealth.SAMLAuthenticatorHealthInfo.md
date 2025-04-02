---
layout: page
title: Data Object - SAMLAuthenticatorHealthInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthInfo`

Returned by
> [SAMLAuthenticatorHealth_Get](vdi.health.SAMLAuthenticatorHealth.md#get), [SAMLAuthenticatorHealth_List](vdi.health.SAMLAuthenticatorHealth.md#list)

See also
> [SAMLAuthenticatorHealthConnectionServerConnectionData](../2406/vdi.health.SAMLAuthenticatorHealth.ConnectionServerConnectionData.md), [SAMLAuthenticatorHealthData](vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthData.md), [SAMLAuthenticatorId](../2406/vdi.entity.SAMLAuthenticatorId.md)

Since
> Horizon View 6.0


## Data Object Description

Information about the health of a SAML authenticator.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [SAMLAuthenticatorId](../2406/vdi.entity.SAMLAuthenticatorId.md)|  The ID of the SAML Authenticator.
**data**| [SAMLAuthenticatorHealthData](vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthData.md)|  Basic information about the SAML authenticator.
**connectionServerData**| [SAMLAuthenticatorHealthConnectionServerConnectionData[]](../2406/vdi.health.SAMLAuthenticatorHealth.ConnectionServerConnectionData.md)|  Information about the SAML authenticator connections from each configured connection server. [^1]
**refId**|  xsd:string|  Reference ID of the SAML Authenticator.  **_Since_** Horizon 7.10 [^1]


 


[^1]: This property need not be set.