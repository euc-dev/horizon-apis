---
layout: page
title: Data Object - CertificateSSOConnectorInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorInfo`

Returned by
> [CertificateSSOConnector_Get](vdi.infrastructure.CertificateSSOConnector.md#get), [CertificateSSOConnector_List](vdi.infrastructure.CertificateSSOConnector.md#list)

See also
> [CertificateSSOConnectorData](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorData.md), [CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md)

Since
> Horizon 7.0


## Data Object Description

Configuration info for a Certificate SSO Connector.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md)|  Reference to this connector. [^2]
**data**| [CertificateSSOConnectorData](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorData.md)|  Configuration data for a Certificate SSO Connector.
**refId**|  xsd:string|  Reference ID used for this Certificate SSO Connector.  **_Since_** Horizon 8.11 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.