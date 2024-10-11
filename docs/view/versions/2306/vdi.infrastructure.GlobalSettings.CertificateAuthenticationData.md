---
layout: page
title: Data Object - GlobalSettingsCertificateAuthenticationData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.CertificateAuthenticationData`

Property of  
> [GlobalSettingsSecurityData](vdi.infrastructure.GlobalSettings.SecurityData.md#field_detail)

Since  
> Horizon 8.10


## Data Object Description 

Supports custom mapping for certificate authentication. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**certAuthMapping**|  xsd:string[]|  Indicates the custom certificate mapping and certificate validation will be done based on all the strings given in certAuthMapping.   


* This property need not be set.

  
**certAuthMappingControl**|  xsd:string[]|  Indicates the types of mapping to validate certificate.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"SID"| Denotes certificate validation on SID.  
"CUSTOM"| Denotes certificate validation on custom mapping.  
"LEGACY"| Denotes legacy certificate validation. In LEGACY mode, the certificate validation is based on User Principal Names(UPN) first, if UPN is unavailable we match X509IssuerSubject or X509SubjectOnly present at altSecurityIdentities attribute of the users Object.  

  
**certAuthMappingNames**|  xsd:string[]|  List of all supported certificate mapping properties.   


* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
