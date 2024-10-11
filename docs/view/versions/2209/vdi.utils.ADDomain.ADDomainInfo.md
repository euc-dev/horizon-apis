---
layout: page
title: Data Object - ADDomainInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.ADDomain.ADDomainInfo`

Returned by  
> [ADDomain_List](vdi.utils.ADDomain.md#list)

See also  
> [ADDomainAdvancedSettings](vdi.utils.ADDomain.ADDomainAdvancedSettings.md), [ADDomainId](vdi.entity.ADDomainId.md), [ServiceAccountCredentials](vdi.utils.ADDomain.ServiceAccountCredentials.md), [ServiceAccountCredentialsInfo](vdi.utils.ADDomain.ServiceAccountCredentialsInfo.md)

Since  
> Horizon View 6.0


## Data Object Description 

Information about an active directory domain. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ADDomainId](vdi.entity.ADDomainId.md)|  The ID of the domain.   
  
**dnsName**|  xsd:string|  The DNS name of the domain.   


* This property cannot be updated.

  
**netBiosName**|  xsd:string|  The NetBIOS name of the domain.   


* This property cannot be updated.

  
**domainType**|  xsd:string|  The relationship of the domain with connection server.  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTION_SERVER_DOMAIN"| The domain having trust with connection server domain.  
"NO_TRUST_DOMAIN"| The domain not having any trust with connection server domain.  

  
**primaryAccount**| [ServiceAccountCredentials](vdi.utils.ADDomain.ServiceAccountCredentials.md)|  Primary service account details. This property will set if domainType is set to "NO_TRUST_DOMAIN".  **_Since_** Horizon 8.1  
  
**auxiliaryAccounts**| [ServiceAccountCredentialsInfo[]](vdi.utils.ADDomain.ServiceAccountCredentialsInfo.md)|  Auxiliary service account details. This property will set if domainType is set to "NO_TRUST_DOMAIN".  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.

  
**adDomainAdvancedSettings**| [ADDomainAdvancedSettings](vdi.utils.ADDomain.ADDomainAdvancedSettings.md)|  Advanced information of No Trust domain. This property will set if domainType is set to "NO_TRUST_DOMAIN".  **_Since_** Horizon 8.1  


* This property need not be set.

  
  
  
 
  
  
