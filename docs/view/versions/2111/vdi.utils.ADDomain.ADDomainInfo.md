---
layout: page
title: Data Object - ADDomainInfo
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.ADDomain.ADDomainInfo`

Returned by
> [ADDomain_List](vdi.utils.ADDomain.md#list)

See also
> [ADDomainAdvancedSettings](vdi.utils.ADDomain.ADDomainAdvancedSettings.md), [ADDomainId](vdi.entity.ADDomainId.md), [ServiceAccountCredentials](vdi.utils.ADDomain.ServiceAccountCredentials.md), [ServiceAccountCredentialsInfo](vdi.utils.ADDomain.ServiceAccountCredentialsInfo.md)

Since
> Horizon View 6.0


## Data Object Description

Information about an active directory domain.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [ADDomainId](vdi.entity.ADDomainId.md)|  The ID of the domain.
**dnsName**|  xsd:string|  The DNS name of the domain. [^2]
**netBiosName**|  xsd:string|  The NetBIOS name of the domain. [^2]
**domainType**|  xsd:string|  The relationship of the domain with connection server.  **_Since_** Horizon 8.1 [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>CONNECTION_SERVER_DOMAIN</td><td>The domain having trust with connection server domain.</td></tr><tr><td>NO_TRUST_DOMAIN</td><td>The domain not having any trust with connection server domain.</td></tr></table>
**primaryAccount**| [ServiceAccountCredentials](vdi.utils.ADDomain.ServiceAccountCredentials.md)|  Primary service account details. This property will set if domainType is set to "NO_TRUST_DOMAIN".  **_Since_** Horizon 8.1
**auxiliaryAccounts**| [ServiceAccountCredentialsInfo[]](vdi.utils.ADDomain.ServiceAccountCredentialsInfo.md)|  Auxiliary service account details. This property will set if domainType is set to "NO_TRUST_DOMAIN".  **_Since_** Horizon 8.1 [^1] [^2]
**adDomainAdvancedSettings**| [ADDomainAdvancedSettings](vdi.utils.ADDomain.ADDomainAdvancedSettings.md)|  Advanced information of No Trust domain. This property will set if domainType is set to "NO_TRUST_DOMAIN".  **_Since_** Horizon 8.1 [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.